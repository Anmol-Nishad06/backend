from django.db import models
from django.utils import timezone

# Create your models here.

Tech_Typyes = [
    ('AI', 'Artificial Intelligence'), 
    ('ML', 'Machine Learning'),
    ('DL', 'Deep Learning'),
    ('NLP', 'Natural Language Processing'),
    ('CV', 'Computer Vision'),
]

class Technology(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    date = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=3, choices=Tech_Typyes, default='AI')
    price= models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    discription = models.TextField(default="No discription curerntly" ,blank=True, null=True)
    def __str__(self):
        return self.name
