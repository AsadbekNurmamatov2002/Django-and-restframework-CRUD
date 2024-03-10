from django.db import models

# Create your models here.


class Product(models.Model):
    name=models.CharField(max_length=250)
    title=models.TextField()
    def __str__(self) -> str:
        return self.name