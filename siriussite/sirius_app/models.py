from django.db import models


class Image(models.Model):
    picture = models.CharField(verbose_name="Картинка")
    description = models.CharField(verbose_name="Описание картинки")

    class Meta:
        verbose_name = "Информация о картинке"
        verbose_name_plural = "Информация о картинках"

    def __str__(self):
        return self.description


