from django.db import models

# Create your models here.

class Register(models.Model):
    id = models.IntegerField(primary_key= True) 
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=15)
    
    class Meta:
        db_table= "users"
    