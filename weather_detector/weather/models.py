from django.db import models



class City(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'cities'