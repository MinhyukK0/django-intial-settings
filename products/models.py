from django.db import models

# Create your models here.

class Menu(models.Model):
	name = models.CharField(max_length=20)

class Category(models.Model):
	name = models.CharField(max_length=20)
	menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

class Product(models.Model):
	name = models.CharField(max_length=100)
	menu = models.ForeignKey('Menu', on_delete=models.CASCADE)
	category = models.ForeignKey('Category', on_delete=models.CASCADE)
