from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.

class Business(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(Neighbourhood, related_name='businesses')
    email = models.EmailField(max_length=30)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('neighbourhood_detail', args=[str(self.id)])
    

    