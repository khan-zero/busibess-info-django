from django.db import models

# Create your models here.
#index models:

class Hero(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=255)
    
    
class OurService(models.Model):
    icon = models.ImageField()
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=255)
    
class AboutUs(models.Model):
    title = models.CharField(max_length=255)
    main_title = models.CharField(max_length=255)
    body = models.TextField(max_length=255)
    
class WhyUs(models.Model):
    icon = models.ImageField()
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=255)
    
class OurTeam(models.Model):
    img = models.ImageField()
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    #social links:
    facebook = models.URLField(max_length=255)
    twitter_x = models.URLField(max_length=255)
    linked_in = models.URLField(max_length=255)
    instagram = models.URLField(max_length=255)
    you_tube = models.URLField(max_length=255)
    
class CustomerReviews(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()


