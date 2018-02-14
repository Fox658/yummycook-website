from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

# Create your models here.
class Platos(models.Model):
    nombre = models.CharField(max_length=250)
    descripcion = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=250, unique=True)
    activo = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Platos, self).save(*args,**kwargs)
    def get_absolute_url(self):
        return reverse('tutoriales:platos', args=[self.slug])
    
    def __str__(self):
        return self.nombre

class ExperienciaEstudiante(models.Model):
    OPCIONES_NIVEL_EXPERIENCIA = (
        ('Principiante', 'Principiante'),
        ('Intermedio','Intermedio'),
        ('Experimentado','Experimentado'),
    ) 
    nivel_experiencia = models.CharField(max_length=20, choices= OPCIONES_NIVEL_EXPERIENCIA, default='Principiante')
    
    def __str__(self):
        return self.nivel_experiencia

class SerieTutoriales(models.Model):
    platos = models.ForeignKey(Platos, on_delete=models.CASCADE)
    experiencia_estudiante = models.ForeignKey(ExperienciaEstudiante, on_delete=models.CASCADE)
    nombre = models.CharField(max_length = 250)
    descripcion = models.TextField(blank=True, null=True)
    archivado = models.BooleanField(default=False)
    slug = models.SlugField(max_length=250, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(SerieTutoriales, self).save(*args,**kwargs)
    
    def get_absolute_url(self):
        return reverse('tutoriales:detalle_serie_tutorial', args=[self.slug])

    def __str__(self):
        return self.nombre

class Leccion(models.Model):
    serie_tutoriales = models.ForeignKey(SerieTutoriales,on_delete=models.CASCADE, related_name='tutoriales')
    titulo = models.CharField(max_length=250)
    video = models.TextField(blank=True, null=True)
    length = models.CharField(max_length=50, blank=True, null=True)
    contenido = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=250, unique=True)
    free_preview = models.BooleanField(default=False)
    activo = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
            self.slug = slugify(self.titulo)
            super(Leccion, self).save(*args,**kwargs) 

    def get_absolute_url(self):
        return reverse('tutoriales:detalle_leccion', args=[self.slug])

    def __str__(self):
        return self.titulo