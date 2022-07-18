from django.db import models

class Bot(models.Model):
    name = models.CharField(max_length=20, blank=False)
    bot_id = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ('name',)
        verbose_name = 'Бот'
        verbose_name_plural = 'Боты'

class Products(models.Model):
    name = models.CharField(max_length=20, blank=False)
    price = models.CharField(max_length=20, blank=False)
    description = models.TextField()
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    src = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
# Create your models here.
