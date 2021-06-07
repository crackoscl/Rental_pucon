from django.contrib import admin
from .models import Usuarios, Vehiculos, Extras, Arriendos

# Register your models here.

admin.site.register(Usuarios)
admin.site.register(Vehiculos)
admin.site.register(Extras)
admin.site.register(Arriendos)
