from django.db import models

# Create your models here.
class Login(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class Information(models.Model):
    name = models.CharField(max_length=20,default="獜洛橙")
    infor = models.CharField(max_length=600)

class Deal_img(models.Model):
    frame = models.ImageField(upload_to='rtn_img')


