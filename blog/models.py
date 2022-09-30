from django.conf import settings
from django.db import models
from django.utils import timezone

"""
Queremos construir un blog. Nuestras entradas de blog necesitan un texto con su contenido y un título, ¿cierto? 
También sería bueno saber quién lo escribió, así que necesitamos un autor. Por último, queremos saber cuándo 
se creó y publicó la entrada. En resumen, tendremos la siguiente estructura:

Post
--------
title
text
author
created_date
published_date
¿Qué tipo de cosas podría hacerse con una entrada del blog? Sería bueno tener algún método que publique la entrada, ¿no?

Así que vamos a necesitar el método publicar ("Post").
"""

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    """
	class Post(models.Model):, esta línea define nuestro modelo (es un objeto).

	class es una palabra clave que indica que estamos definiendo un objeto.
	Post es el nombre de nuestro modelo. Podemos darle un nombre diferente (pero debemos evitar espacios en blanco y caracteres especiales). Siempre inicia el nombre de una clase con una letra mayúscula.
	models.Model significa que Post es un modelo de Django, así Django sabe que debe guardarlo en la base de datos.

	Ahora definimos las propiedades de las que hablábamos: title, text, created_date, published_date y author. 
	Para ello tenemos que definir el tipo de cada campo (¿es texto? ¿un número? ¿una fecha? 
	¿una relación con otro objeto como un User (usuario)?)

	models.CharField, así es como defines un texto con un número limitado de caracteres.
	models.TextField, este es para texto largo sin límite. Suena perfecto para el contenido de la entrada del blog, ¿no?
	models.DateTimeField, este es fecha y hora.
	modelos.ForeignKey, este es una relación (link) con otro modelo.
    """

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    """
	¿Y qué sobre def publish(self):? Es exactamente el método publish que mencionábamos antes. 
	def significa que es una función/método y publish es el nombre del método. 
    """

    def __str__(self):
        return self.title
        #Los métodos suelen devolver (return, en inglés) algo. Hay un ejemplo de esto en el método __str__. 
        #En este escenario, cuando llamemos a __str__() obtendremos un texto (string) con un título de Post.

        #Esta funcion es entendida por Python con este nombre. Es como una especie de funcion predefinida.
        #Si le cambio el nombre, y le pongo print al objeto ("print("Post")"), me va a entregar algo por defecto, 
        #y no lo que hace python.