from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.

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