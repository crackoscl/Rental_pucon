
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import RegisterUserForm, ArrendarForm
from .models import Vehiculos, Extras, Usuarios, Arriendos
from django.utils import timezone
from .user_permissions import is_trabajador, rol_usuario


class Principal(LoginRequiredMixin, UserPassesTestMixin, View):
    login_url = '/login/'
    template_name = 'app/index.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_trabajador:
            vehiculos = Vehiculos.objects.all()
            return render(request, self.template_name, {'vehiculos': vehiculos})
        else:
            vehiculos = Vehiculos.objects.filter(estado='disponible')
            return render(request, self.template_name, {'vehiculos': vehiculos})

    def test_func(self):
        return rol_usuario(self.request.user)


class Arrendar(LoginRequiredMixin, UserPassesTestMixin, View):
    login_url = '/login/'
    template_name = 'app/arrendar.html'

    def get(self, request, *args, **kwargs):
        auto = get_object_or_404(Vehiculos, pk=self.kwargs['pk'])
        return render(request, self.template_name, {'pk': auto})

    def post(self, request, *args, **kwargs):
        vehiculo = Vehiculos.objects.get(id=self.kwargs['pk'])
        usuario = vehiculo.usuario_id
        vehiculo.estado = 'arrendado'
        vehiculo.save()
        Arriendos.objects.create(
            usuario_id=usuario,
            vehiculo_id=vehiculo
        )
        return redirect('app:principal')

    def test_func(self):
        return is_trabajador(self.request.user)


class Devolver(LoginRequiredMixin, UserPassesTestMixin, View):
    login_url = '/login/'
    template_name = 'app/devolver.html'

    def get(self, request, *args, **kwargs):
        arriendo = get_object_or_404(
            Arriendos, vehiculo_id=self.kwargs['pk'], fecha_termino=None)

        form = ArrendarForm(instance=arriendo)
        return render(request, self.template_name, {'form': form, 'pk': arriendo})

    def post(self, request, *args, **kwargs):
        form = ArrendarForm(request.POST)
        if form.is_valid():
            formulario_data = form.cleaned_data
            arriendo = Arriendos.objects.get(id=kwargs['pk'])
            vehiculo = arriendo.vehiculo_id
            fecha_termino = timezone.now()
            diferencia_hora = fecha_termino - arriendo.fecha_inicio
            total_segundos = diferencia_hora.seconds
            minutos = total_segundos / 60
            precio_dia = vehiculo.precio_dia
            precio_hora = precio_dia / 24
            precio_minuto = precio_hora / 60
            precio = round(precio_minuto * minutos)
            arriendo.observaciones = formulario_data['observaciones']
            arriendo.precio = precio
            arriendo.fecha_termino = fecha_termino
            arriendo.save()
            vehiculo.estado = 'disponible'
            vehiculo.save()

            return redirect('app:principal')
        else:
            form = ArrendarForm()
            return render(request, self.template_name, {'form': form})

    def test_func(self):
        return is_trabajador(self.request.user)


class Reservar(LoginRequiredMixin, UserPassesTestMixin, View):
    login_url = '/login/'
    template_name = 'app/reservar.html'

    def get(self, request, *args, **kwargs):
        auto = get_object_or_404(Vehiculos, pk=self.kwargs['pk'])
        extras = auto.extras_set.all()
        return render(request, self.template_name, {'pk': auto, 'extras': extras})

    def post(self, request, *args, **kwargs):
        vehiculos = Vehiculos.objects.get(id=self.kwargs['pk'])
        vehiculos.estado = 'reservado'
        vehiculos.usuario_id = Usuarios.objects.get(id=request.user.id)
        vehiculos.save()

        return redirect('app:principal')

    def test_func(self):
        return rol_usuario(self.request.user)


class Ver_ficha(LoginRequiredMixin, UserPassesTestMixin, View):
    login_url = '/login/'
    template_name = 'app/verficha.html'

    def get(self, request, *args, **kwargs):
        auto = get_object_or_404(Vehiculos, pk=self.kwargs['pk'])
        extras = auto.extras_set.all()
        return render(request, self.template_name, {'pk': auto, 'extras': extras})

    def test_func(self):
        return is_trabajador(self.request.user)


def registro(request):
    context = {
        'form': RegisterUserForm()
    }
    if request.method == 'POST':
        form = RegisterUserForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)
            return redirect(to='app:principal')
        else:
            context['form'] = form
    return render(request, 'registration/registro.html', context)
