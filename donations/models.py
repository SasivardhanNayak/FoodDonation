from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class food(models.Model):
    food_id = models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/')
    name=models.CharField(max_length=50)
    food_type=models.CharField(max_length=20)
    category=models.CharField(max_length=20)
    qnt=models.PositiveIntegerField()
    status=models.BooleanField(default=True)
    donate=models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.name}"



class cloths(models.Model):
    cloth_id = models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/')
    name=models.CharField(max_length=50)
    cloth_type=models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    qnt=models.PositiveIntegerField()
    status=models.BooleanField(default=True)
    def __str__(self):
        return f"{self.name}"

class Donation_Request(models.Model):
    request_id = models.AutoField(primary_key=True)
    request_type=models.CharField(max_length=20)
    item_id=models.IntegerField()
    donar=models.ForeignKey(User,on_delete=models.CASCADE,related_name='donations')
    user=models.ForeignKey(User,on_delete=models.CASCADE, related_name='donation_requests')
    Address= models.CharField(max_length=512)
    contact=models.PositiveIntegerField()
    donate_status=models.BooleanField(default=False)
    def __str__(self):
        return f"{self.user} request"

