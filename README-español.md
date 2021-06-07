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
_Instalar dependecias._

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



_Que cosas necesitas para instalar el software y como instalarlas_

```
Da un ejemplo
```

## Licencia 📄

Este proyecto está bajo la Licencia (GPLv3)

## Expresiones de Gratitud 🎁

* Comenta a otros sobre este proyecto 📢
* Invita una cerveza 🍺 o un café ☕ a alguien del equipo. 
* Da las gracias públicamente 🤓.
* etc.


---
⌨️ con ❤️ por [Crackoscl](https://github.com/crackoscl) 😊
