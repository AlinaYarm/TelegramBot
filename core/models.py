from django.db import models


class User(models.Model):
    user_id = models.IntegerField('ID', primary_key=True)
    username = models.CharField('User_name', max_length=32, null=True, blank=True)
    first_name = models.CharField('Name', max_length=256, null=True, blank=True)
    last_name = models.CharField('Surname', max_length=256, null=True, blank=True)
    created_at = models.DateTimeField('Создан', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлен', auto_now=True)


    def __str__(self):
        return f'@{self.username}' if self.username is not None else f'{self.user_id}'

    class Meta:
        verbose_name = 'Пользователь чат бота'
        verbose_name_plural = 'Пользователи чат бота'

class Person(models.Model):
    user_code = models.IntegerField('Code', primary_key=True)
    username = models.CharField('User_name', max_length=32, null=True, blank=True)

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'


    def __str__(self):
        return f'@{self.username}' if self.username is not None else f'{self.user_code}'