from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    bio = models.CharField(max_length=255)
    profile_pic = models.ImageField(upload_to='profile/')
    pub_date_created = models.DateTimeField(auto_now_add=True, null=True)
    neighbourhood = models.ForeignKey('Neighbourhood', blank=True, null=True)

class Business(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    neighbourhood = models.ForeignKey(Neighbourhood, related_name='businesses')
    email = models.EmailField(max_length=30)
    image = models.ImageField(upload_to='bizimage/')
    
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