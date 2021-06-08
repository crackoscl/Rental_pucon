# Rental Pucon

_Prueba de salida talento digital para chile._

## Comenzando 🚀

_Clonar el Proyecto_

```
$ git clone https://github.com/crackoscl/Rental_pucon.git
$ cd Rental_pucon
```
_Crear y Activar entorno virtual._

```
$ virtualenv venv
$ source venv/bin/activate

```
_Instalar dependencias._

```
$ pip install -r requeriments.txt
```

_Agregar archivo .env en carpeta rental_pucon._

```
DEBUG=True
SECRET_KEY=django-insecure-k0^(-uulsdvvr%fj)p@*azebx)jd3ueallalahsswdedkewhdweklz^
ALLOWED_HOSTS=127.0.0.1,localhost
POSTGRES_DB=nombrebasededatos
POSTGRES_USER=usuariopostgres
POSTGRES_PASSWORD=1we2342122
POSTGRES_HOST=localhost
POSTGRES_PORT=puertopostgress
```

_Migraciones._

```
$ python manage.py makemigrations app
$ python manage.py migrations app
$ python manage.py makemigrations 
$ python manage.py migrate

```
_Creacion de Super Usuario._

```
$ python manage.py createsuperuser
```

_Inicio del servidor de desarrollo._

```
$ python manage.py runserver
```

## Capturas 📖

_LOGIN._
![Login](https://github.com/crackoscl/Rental_pucon/blob/main/screenshot%201.png?raw=true "Login Usuarios")

_USUARIO CLIENTE._
![Cliente](https://github.com/crackoscl/Rental_pucon/blob/main/screenshot%202.png?raw=true "Usuario Cliente")

_RESERVA VEHÍCULO CLIENTE._
![Reserva Vehículo Cliente](https://github.com/crackoscl/Rental_pucon/blob/main/screenshot%203.png?raw=true "Reserva Vehículo Cliente")

_USUARIO TRABAJADOR._
![Usuario Trabajador](https://github.com/crackoscl/Rental_pucon/blob/main/screenshot%204.png?raw=true "Usuario Trabajador")

_CONFIRMACIÓN DE ARRIENDO._
![Confirmación de Arriendo](https://github.com/crackoscl/Rental_pucon/blob/main/screenshot%205.png?raw=true "Confirmación de Arriendo")

_FORMULARIO DE DEVOLUCÍON._
![Formulario Devolucíon](https://github.com/crackoscl/Rental_pucon/blob/main/screenshot%206.png?raw=true "Formulario de Devolucíon")

_FORMULARIO DE REGISTRO._
![Formulario Registro](https://github.com/crackoscl/Rental_pucon/blob/main/screenshot%207.png?raw=true "Formulario de Registro")


## Licencia 📄

Este proyecto está bajo la Licencia (GPLv3)


---
⌨️ con ❤️ por [Crackoscl](https://github.com/crackoscl) 😊
