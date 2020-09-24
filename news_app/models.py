from django.db import models
import datetime
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

CATEGORY_CHOICES = (
    ('World','World'),
    ('Country','Country'),
    ('Sports','Sports'),
    ('Business','Business'),
    ('Carrier','Carrier'),
    ('Entertainment','Entertainment'),
    ('Tech','Tech'),
    ('Startup','Startup'),
    ('Politics','Politics'),   

)

class Country(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,default=1 )
    image = models.ImageField(upload_to='pics_country', null=True)
    heading = models.CharField(max_length=100)
    title=models.CharField(max_length=500)
    content = models.TextField()
    date_time = models.DateTimeField(default=datetime.datetime.now()) 
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)


    
    def get_absolute_url(self):
        return reverse('country-detail', kwargs={'pk': self.pk})

    
   

