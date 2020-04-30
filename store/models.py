from django.db import models
from django.contrib.postgres.fields import JSONField

class Category(models.Model):
	name = models.CharField("Категория", max_length = 255)
	parent = models.ForeignKey('self', verbose_name = "Родитель", on_delete = models.SET_NULL, blank = True, null = True)
	url = models.SlugField("Ссылка", max_length = 150, unique = True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Категория"
		verbose_name_plural = "Категории"

class Product(models.Model):
	name = models.CharField("Название", max_length = 255)
	price = models.DecimalField("Цена", max_digits = 19, decimal_places=2)
	description = models.TextField("Описание")
	url = models.SlugField("Ссылка", max_length = 150, unique = True)
	category = models.ForeignKey(Category, verbose_name = "Категория", on_delete = models.SET_NULL, null = True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['id']
		verbose_name = "Товар"
		verbose_name_plural = "Товары"

class Picture(models.Model):
	product = models.ForeignKey(Product, verbose_name = "Товар", on_delete = models.CASCADE)
	description = models.TextField("Описание")
	name = models.CharField("Заголовок", max_length = 255)
	image = models.ImageField("Изображение", upload_to="images/")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Изображение"
		verbose_name_plural = "Изображения"

class Value(models.Model):
	value = models.CharField("Значение", max_length = 100)

	def __str__(self):
		return self.value

	class Meta:
		verbose_name = "Значение"
		verbose_name_plural = "Значения"

class Feature(models.Model):
	name = models.CharField("Название", max_length = 255)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Характеристика"
		verbose_name_plural = "Характеристики"

class ProductFeatureValue(models.Model):
	product = models.ForeignKey(Product, verbose_name = "Товар", on_delete = models.CASCADE)
	feature = models.ForeignKey(Feature, verbose_name = "Характеристика", on_delete = models.CASCADE)
	value = models.ForeignKey(Value, verbose_name = "Значение", on_delete = models.CASCADE)

	class Meta:
		verbose_name = "Характеристика товара"
		verbose_name_plural = "Характеристики товаров"
