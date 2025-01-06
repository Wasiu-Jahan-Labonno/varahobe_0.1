from django.db import models
from accounts.models import User



class Clothing(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Clothing')
    title = models.CharField(max_length=100)
    description = models.TextField()
    area = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='clothing_images/')

    def __str__(self):
        return self.title
# Create your models here.

