from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Barber(models.Model):
    image = models.ImageField(upload_to='barbers')
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    about = models.CharField(max_length=255)
    facebook = models.URLField(max_length=255)
    instagram = models.URLField(max_length=255)

    def __str__(self):
        return self.full_name


class Testimonial(models.Model):
    image = models.ImageField(upload_to='barbers')
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.full_name


class Service(models.Model):
    image = models.ImageField(upload_to='services')
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.title


class Appointment(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255)
    datetime = models.DateTimeField()
    comment = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name


class Contact(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255)
    datetime = models.DateTimeField()
    comment = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name


class Subscribe(models.Model):
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.email
