from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        max_length=200, verbose_name='Название группы',
        help_text='Укажите название группы')
    description = models.TextField(
        verbose_name='Описание группы',
        help_text='Введите описание группы')
    slug = models.SlugField(
        unique=True, verbose_name='URL-адрес группы',
        help_text='Укажите уникальный URL-адрес')

    class Meta:
        verbose_name_plural = 'Сообщества'
        verbose_name = 'Сообщество'

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(
        verbose_name='Текст', help_text='Пишите здесь ваш текст')
    pub_date = models.DateTimeField(
        auto_now_add=True, verbose_name='Опубликовано',
        help_text='Дата создания записи')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts',
        verbose_name='Автор',
        help_text='Укажите автора')
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL,
        related_name='group_posts', blank=True, null=True,
        verbose_name='Сообщество',
        help_text='Выберите сообщество')

    class Meta:
        ordering = ('-pub_date',)
        verbose_name_plural = 'Записи'
        verbose_name = 'Запись'

    def __str__(self):
        return self.text
