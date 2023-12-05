from django.db import models

class patient_detail(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField(default=0)
    gender=models.CharField(max_length=10)
    disease=models.CharField(max_length=30)

    def __str__(self):
      return self.name
# Create your models here.
