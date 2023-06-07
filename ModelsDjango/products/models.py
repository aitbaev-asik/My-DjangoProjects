from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    age = models.IntegerField(verbose_name='Возраст')
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True,verbose_name='Номер телефона')

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author: Person = models.ForeignKey(Person, on_delete=models.CASCADE)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return f'Book: {self.title} - Author: {self.author.full_name}'


class Order(models.Model):
    customer: Person = models.ForeignKey(Person, on_delete=models.CASCADE)
    book: Book = models.ForeignKey(Book, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.book.title} {self.customer.full_name}"
