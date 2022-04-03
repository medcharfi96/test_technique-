from django.db import models
from django.urls import reverse
from setuptools.command.upload import upload
from django.core.exceptions import ValidationError



class compte(models.Model):
    nom = models.CharField(max_length=200,blank=False, verbose_name="nom")
    prenom = models.CharField(max_length=200,blank=False, verbose_name="prenom")
    age = models.IntegerField(blank=False)
    profile = models.URLField(verbose_name="profile")
    lettre_de_motivation = models.TextField(max_length=500, verbose_name="lettre_motivation")
    CV = models.FileField(upload_to='prof')


    def get_absolute_url(self):
        return reverse('prof:create')

    def save(self, *args, **kwargs):
        if self.CV.size >5242880:
            raise ValidationError("The maximum file size that can be uploaded is 5MB")
        super().save(*args, **kwargs)



class CV_Text(models.Model):
    TextCV = models.TextField(max_length= 5000, verbose_name="cvtext")