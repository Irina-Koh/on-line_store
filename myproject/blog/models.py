from django.db import models



class BlogPost(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name='Заголовок',
        help_text='Введите заголовок'
    )
    is_published = models.BooleanField(
        default=True
    )

    content = models.TextField(
        verbose_name='Содержимое',
        help_text='Введите содержимое статьи'
    )
    preview_image = models.ImageField(
        upload_to='blog_preview/photo',
        verbose_name='Изображение',
        help_text='Загрузите изображение',
        blank=True,
        null=True
    )
    views_counter = models.PositiveIntegerField(
        verbose_name='Счетчик просмотров',
        help_text='Укажите количество просмотров',
        default=0,
    )

    created_at = models.DateTimeField(
        verbose_name='Опубликовано',
        auto_now_add=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блоговая запись'
        verbose_name_plural = 'Блоговые записи'
        ordering = ['-created_at']  # Сортировка по дате создания (новые сверху)
