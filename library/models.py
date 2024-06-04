from django.db import models
from django.urls import reverse

# Create your models here.
class Lib(models.Model):

    name = models.TextField()
    author = models.TextField()
    publishing = models.TextField()
    genre = models.TextField()
    year = models.IntegerField()
    review = models.TextField(blank = True)
    rate = models.IntegerField(blank = True)
    read = models.BooleanField(default=False)
    picture = models.URLField()

    def __str__(self):
        """Строка для представления объекта Lib (например, в административной панели и т.д.)."""
        return self.name

    class Meta:
        ordering = ['-id']

    def get_absolute_url(self):
        """Возвращает URL-адрес для доступа к определенному экземпляру Lib."""
        return reverse('model-detail-view', args=[str(self.id)])