from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=30)  #название поста и макс кол-во символов
    description = models.TextField()
    tags = models.CharField(max_length=25) #описываем теги проекта огранич по длине
    image = models.FileField(upload_to='img/') #прописываем где храниться кэш картинок 'img/' папка каталог где храняться картинки

# Create your models here.
