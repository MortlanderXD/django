from django.contrib import admin
from .models import Personne, Message
# Register your models here.


class PersonneAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{"fields" : ["nom"]}),
        ("prenom", {"fields": ["prenom"]}),
        ("date de naissance", {"fields": ["date_de_naissance"]}),
        ("courriel", {"fields": ["courriel"]}),
        ("tel fixe", {"fields": ["tel_fixe"]}),
        ("tel mobile", {"fields": ["tel_mobile"]}),
        ("password", {"fields": ["mot_de_passe"]}),
        ("Amis", {"fields": ["amis"]}),
                 ] 

class MessageAdmin(admin.ModelAdmin):
     fieldsets = [
         ("auteur", {"fields": ["auteur"]}),
         ("contenu", {"fields": ["contenu"]}),
         ("date de publication", {"fields": ["date_de_publication"]}),  
    ]
    

admin.site.register(Personne, PersonneAdmin)
admin.site.register(Message,MessageAdmin)