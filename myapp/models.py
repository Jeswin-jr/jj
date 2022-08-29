from django.db import models
class customer(models.Model):
    name=models.CharField(max_length=88)
    address=models.TextField(max_length=88)
    age=models.IntegerField()
    email=models.EmailField()
    def __str__(self):
        return self.name

# Create your models here.
