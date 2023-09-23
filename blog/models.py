from django.db import models

# Create your models here.
class Home(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255,blank=True,null=True)
    about = models.TextField()
    copyright = models.CharField(max_length=255,blank=True,null=True)
    address = models.CharField(max_length=255,blank=True,null=True)
    phone = models.CharField(max_length=255,blank=True,null=True)
    email = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.title
    
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255,blank=True,null=True)
    last_name = models.CharField(max_length=255,blank=True,null=True)
    email = models.CharField(max_length=255,blank=True,null=True)
    subject = models.CharField(max_length=255,blank=True,null=True)
    message = models.CharField(max_length=2000,blank=True,null=True)

    def __str__(self):
        return self.first_name