from django.db import models
from django.contrib.auth.models import AbstractUser

from materials.models import Course, Lesson


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    def __str__(self):
        return self.email


class Payments(models.Model):
    PAYMENT_STATUS = [
        ("cash", "наличные"),
        ("transfer", "перевод на счет"),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user', verbose_name="Пользователь")
    payment_date = models.DateField(null=True, blank=True, verbose_name="Дата оплаты")
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course', verbose_name="Оплаченный курс", null=True, blank=True)
    separately_paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='lesson', verbose_name="Оплаченный урок", null=True, blank=True)
    payment_amount = models.IntegerField(default=0, verbose_name="Сумма оплаты", null=True, blank=True)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_STATUS, default="cash", verbose_name="Способ оплаты", null=True, blank=True)
    session_id = models.CharField(max_length=255, verbose_name='Id сессии', help_text='Укажите id сессии', null=True, blank=True)
    link = models.URLField(max_length=400, verbose_name='Ссылка на оплату', help_text='Укажите ссылку на оплату',
                           null=True, blank=True)

    def __str__(self):
        return f'{self.user} {self.paid_course}'

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
