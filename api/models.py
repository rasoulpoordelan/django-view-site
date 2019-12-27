from django.db import models
from tinymce.models import HTMLField

class TrainInfo(models.Model):
    train_num=models.CharField(max_length=50,unique=True)
    name=models.CharField(max_length=200)
    props=models.ManyToManyField('Prop')
    description=HTMLField(null=True)
    short_description=models.CharField(max_length=500,null=True)


    def __str__(self):
        return self.name

class Image(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='images/')
    train_info=models.ForeignKey(TrainInfo,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Prop(models.Model):
    name=models.CharField(max_length=100)
    priority=models.IntegerField()
    def __str__(self):
        return self.name
    




