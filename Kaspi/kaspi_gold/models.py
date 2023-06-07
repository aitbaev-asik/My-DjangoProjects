from django.db import models
from django.forms import ValidationError
from .utils import validate_iin, validate_phone_number


class User(models.Model):
    first_name: str = models.CharField(max_length=32, verbose_name='Имя')
    last_name: str = models.CharField(max_length=32, verbose_name='Фамилия')
    balance = models.IntegerField(default=0)
    phone = models.CharField(max_length=32, unique=True,validators=[validate_phone_number], verbose_name='Номер телефона')
    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True, verbose_name='Фото')
    iin = models.CharField(max_length=12, verbose_name='IIN', unique=True, validators=[validate_iin])
    birth_date = models.DateField(verbose_name='Дата рождения')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def clean(self):
        date = self.birth_date.strftime('%y%m%d')
        if self.iin[:6] != date:
            raise ValidationError('Неверный ИИН')

    def __str__(self):
        return f"{self.first_name.title()} {self.last_name.title()[0]}."


class Transaction(models.Model):
    sender: User = models.ForeignKey(User, on_delete=models.PROTECT, related_name='sent_transactions')
    recipient: User = models.ForeignKey(User, on_delete=models.PROTECT, related_name='received_transactions')
    sum = models.IntegerField(verbose_name='Сумма')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')

    def __str__(self):
        return f"{self.sender} to {self.recipient} sum: {self.sum}"

    def clean(self):
        if self.sender == self.recipient:
            raise ValidationError('Вы не можете отправить деньги самому себе')

        if self.sum < 100:
            raise ValidationError('Минимальная сумма отправки 100Т')

        if self.sender.balance < self.sum:
            raise ValidationError('На вашем счету не хватает средств')

    def save(self, *args, **kwargs):
        self.sender.balance -= self.sum
        self.recipient.balance += self.sum
        self.sender.save()
        self.recipient.save()
        super().save(*args, **kwargs)
