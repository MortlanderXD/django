from django.db import models

# Create your models here.

from django.db import models

# Create your models here.
class Personne(models.Model ): 
    nom = models.CharField(max_length=30) 
    prenom = models.CharField(max_length=30) 
    date_de_naissance = models.DateField() 
    courriel = models.EmailField() 
    tel_fixe = models.CharField(max_length=20) 
    tel_mobile = models.CharField(max_length=20) 
    mot_de_passe = models.CharField(max_length=32) 
    amis = models.ManyToManyField("self",blank=True)
    
    def __str__(self):
        return self.nom + ' ' + self.prenom

class Message(models.Model) : 
    auteur = models.ForeignKey(Personne,on_delete=models.CASCADE)
    contenu = models .TextField() 
    date_de_publication = models .DateField() 
    
    def __str__(self):
        return self.auteur.nom + ' '+ self.auteur.prenom + ' : ' + self.contenu