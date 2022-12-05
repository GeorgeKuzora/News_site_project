from django.db import models
from django.contrib.auth.models import User
from django.forms import TextInput

# Create your models here.


class News(models.Model):
    POLITICS = 'PL'
    SPORT = 'SP'
    BUSINESS = 'BS'
    ENTERTAINMENT = 'EN'
    LOCAL = 'LO'
    NEWS_CHOICES = [
        (POLITICS, 'Politics'),
        (SPORT, 'Sport'),
        (BUSINESS, 'Business'),
        (ENTERTAINMENT, 'Entertainmen'),
        (LOCAL, 'Local'),
    ]
    title = models.CharField(max_length=100, verbose_name='заголовок', db_index=True)
    content = models.TextField(max_length=10000, verbose_name='текст новости')
    creation_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата обновления')
    is_active = models.BooleanField(default=False, verbose_name='статус')
    tag = models.CharField(choices=NEWS_CHOICES, default=LOCAL, verbose_name='тэг')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['creation_at']


class Commentaries(models.Model):
    user_name = models.CharField(max_length=200, default='anonim', blank=True, verbose_name='имя пользователя')
    commentary = models.CharField(max_length=500, verbose_name='комментарий')
    connected_news = models.ForeignKey(News, on_delete=models.SET_DEFAULT, default='Такой новости нет', verbose_name='имя новости')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='имя зарегистрированого пользователя')

    def __str__(self):
        return self.user_name
