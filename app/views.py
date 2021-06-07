
from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .forms import RegisterUserForm,ArrendarForm
from .models import Vehiculos,Extras,Usuarios,Arriendos
from django.contrib.auth import get_user_model
from django.utils import timezone

def rol_usuario(user):
    if not user.is_superuser:
        return user

def is_trabajador(user):
    return user.is_trabajador

class Principal(LoginRequiredMixin,UserPassesTestMixin,View):
    login_url = '/login/'
    template_name = "app/index.html"
    def get(self, request, *args, **kwargs):
        if request.user.is_trabajador:
            vehiculos = Vehiculos.objects.all()
            return render(request,self.template_name,{"vehiculos":vehiculos})
        else:
            vehiculos = Vehiculos.objects.filter(estado='disponible')
            return render(request,self.template_name,{"vehiculos":vehiculos})
    def test_func(self):
        return rol_usuario(self.request.user)

        
class Arrendar(LoginRequiredMixin,UserPassesTestMixin,View):
    login_url = '/login/'
    template_name = "app/arrendar.html"
    def get(self, request, *args, **kwargs):
        auto = get_object_or_404(Vehiculos, pk=self.kwargs['pk'])
        return render(request,self.template_name,{"pk":auto})

    def post(self, request, *args, **kwargs):
        vehiculo = Vehiculos.objects.filter(id=self.kwargs['pk'])
        v_arriendo = list(vehiculo)
        usuario = Usuarios.objects.get(id=v_arriendo[0].usuario_id_id)
        a_vehiculo = Vehiculos.objects.get(id=v_arriendo[0].id)
        vehiculo.update(
            estado = 'arrendado',
        )
        print(usuario)
        Arriendos.objects.create(
            usuario_id  = usuario,
            vehiculo_id = a_vehiculo
        )
        return redirect('app:principal')

    def test_func(self):
        return is_trabajador(self.request.user)



class Devolver(LoginRequiredMixin,UserPassesTestMixin,View):
    login_url = '/login/'
    template_name = "app/devolver.html"

    def get(self, request, *args, **kwargs):
        arriendo = get_object_or_404(Arriendos,vehiculo_id=self.kwargs['pk'])
        form = ArrendarForm(instance=arriendo)
        return render(request,self.template_name,{'form':form,'pk':arriendo})

    def post(self, request, *args, **kwargs):
        form = ArrendarForm(request.POST)
        if form.is_valid():
            formulario_data = form.cleaned_data
            arriendo = Arriendos.objects.filter(id=kwargs['pk'])
            vehiculo = arriendo[0].vehiculo_id
            arriendo.update(
                observaciones = formulario_data['observaciones'],
                precio = 4560,
                fecha_termino = timezone.now()
            )
            vehiculo = Vehiculos.objects.filter(id=vehiculo.id).update(
                estado = 'disponible',
            )
            return redirect('app:principal')

        else:
            form = ArrendarForm()
            return render(request,self.template_name,{'form':form})

    def test_func(self):
        return is_trabajador(self.request.user)


class Reservar(LoginRequiredMixin,View):
    login_url = '/login/'
    template_name = "app/reservar.html"
    def get(self, request, *args, **kwargs):
        auto = get_object_or_404(Vehiculos, pk=self.kwargs['pk'])
        extras = auto.extras_set.all()
        return render(request,self.template_name,{"pk":auto,'extras':extras})

    def post(self, request, *args, **kwargs):
        Vehiculos.objects.filter(id=self.kwargs['pk']).update(
            estado = 'reservado',
            usuario_id = request.user.id
        )
        return redirect('app:principal')

class Ver_ficha(LoginRequiredMixin,View):
    login_url = '/login/'
    template_name = "app/verficha.html"
    def get(self, request, *args, **kwargs):
        auto = get_object_or_404(Vehiculos, pk=self.kwargs['pk'])
        extras = auto.extras_set.all()
        return render(request,self.template_name,{"pk":auto,'extras':extras})
    
    def test_func(self):
        return is_trabajador(self.request.user)


def registro(request):
    context = {}
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="app:principal")
        else:
            context['form'] = RegisterUserForm
    else:
        form = RegisterUserForm()
        context['form'] = form
    return render(request, 'registration/registro.html', context)