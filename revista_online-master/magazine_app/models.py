from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class StoryManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(models.Q(name__icontains=query) | models.Q(description__icontains=query))

class MagazineApp(models.Model): #Modelo de las historias
    manage = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    title = models.CharField('Título', max_length=120)
    slug = models.SlugField('Atajo')
    synopsis = models.TextField('Sinopsis', blank=True, null=True)
    author = models.CharField('Autor', max_length=120)
    genre = models.CharField('Género', max_length=120)

    objects = StoryManager()

    '''def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('story:details', args=(self.slug,))'''

    class Meta:
        verbose_name = 'Historia'
        verbose_name_plural = 'Historias'
        ordering = ['title']