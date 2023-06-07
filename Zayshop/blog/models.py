from django.db import models


class HomeProduct(models.Model):
    img = models.ImageField(upload_to='index')
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.name


class MonthProduct(models.Model):
    img = models.ImageField(upload_to='index')
    name = models.CharField(max_length=255)
    button = models.URLField(max_length=255)

    def __str__(self):
        return self.name


class FeaturedProduct(models.Model):
    img = models.ImageField(upload_to='index')
    price = models.FloatField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.name


class Gender(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='brands')

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='categories')

    def __str__(self) -> str:
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    # student: Student = models.ForeignKey(Student, on_delete=models.PROTECT, related_name='Ученик')

    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    category = models.ManyToManyField(Category)
    size = models.ManyToManyField(Size, null=True)
    price = models.FloatField()
    img = models.ImageField(upload_to='products')
    description = models.CharField(max_length=1000)
    specificaiton = models.CharField(max_length=1000)
    gender = models.ForeignKey(Gender, on_delete=models.PROTECT, null=True)

    def __str__(self) -> str:
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField(max_length=255)

    def __str__(self):
        return self.name


class Subscribe(models.Model):
    email = models.EmailField(max_length=255)

