from django.db import models
from datetime import datetime

# Create your models here.
class contact (models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    car_id = models.IntegerField()
    customer_need = models.CharField(max_length=300)
    car_title = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    state = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)
    phone = models.CharField(max_length=300)
    messege = models.TextField(blank=True)
    user_id = models.CharField(blank=True, max_length=300)
    created_date = models.DateTimeField(blank=True, default=datetime.now)
    
    def __str__(self):
        return self.email
