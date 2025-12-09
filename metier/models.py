from django.db import models

# Create your models here.
class Piece(models.Model):
    nom =models.CharField(max_length=100)
    prix=models.FloatField()


class Reparation(models.Model):
    piece=models.ForeignKey(Piece,on_delete=models.CASCADE)
    duree=models.IntegerField()
    
class Voiture(models.Model):
    marque=models.CharField(max_length=100)
    couleur=models.CharField(max_length=10,default="")