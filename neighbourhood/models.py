from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    bio = models.CharField(max_length=255, default="I love my Hood !!")
    profile_pic = models.ImageField(upload_to='profile/')
    pub_date_created = models.DateTimeField(auto_now_add=True, null=True)
    neighbourhood = models.ForeignKey('Neighbourhood', blank=True, null=True)
    
    def __str__(self):
        return self.first_name
    def save_profile(self):
        self.save()
    def delete_profile(self):
        self.delete()
        
class Neighbourhood(models.Model):
    name = models.CharField(max_length = 255)
    location = models.CharField(max_length=255)
    occupants = models.IntegerField()
    image = models.ImageField(upload_to='neighimage/', null=True)
    admin = models.ForeignKey(Profile, related_name='hoods', null=True)
    description = models.CharField(max_length = 300,default='My hood!!!')
    
    
    def save_neighbourhood(self):
        self.save()
    def delete_neighbourhood(self):
        self.delete()
        
class Business(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    neighbourhood = models.ForeignKey(Neighbourhood, related_name='businesses')
    email = models.EmailField(max_length=30)
    image = models.ImageField(upload_to='bizimage/')
    profile = models.ForeignKey(Profile, related_name='profiles')
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('neighbourhood_detail', args=[str(self.id)])
    
    def save_business(self):
        self.save()
    
    def delete_business(self):
        self.delete()
        
    @classmethod
    def search_by_name(cls, search_term):
        business = cls.objects.filter(title__icontains=search_term)
        return business
        



    
