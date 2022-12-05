from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField('телефон', max_length=12, blank=True)
    city = models.CharField('город', max_length=30, blank=True)
    verification_mark = models.BooleanField('Верификация', default=False)
    number_of_posted_news = models.IntegerField('количество опубликованных новостей', default=0)
    date_of_birth = models.DateField('дата рождения', blank=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        permissions = (
                ("can_post_news", "Может публиковать новости"),
                ("can_verify", "Может верифицировать"),
                )

    def __str__(self):
        return self.user
