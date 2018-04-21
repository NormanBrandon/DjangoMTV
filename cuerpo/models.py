from django.db import models
# Create your models here.
from django.utils import timezone
class Post(models.Model):
    autor = models.ForeignKey('auth.User',on_delete = models.CASCADE)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fechaCreacion = models.DateTimeField(
        default=timezone.now
    )
    fechaPublicacion = models.DateTimeField(
        blank=True,null =True

    )
    def publicar(self):
        self.fechaPublicacion = timezone.now()
        self.save()
    #Metodo magico que nos permite castear un objeto a una cadena
    def __str__(self):
        return self.titulo
