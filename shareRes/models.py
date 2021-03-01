from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length = 100)

    def __str__(self):
        return self.category_name

class Restaurant(models.Model):
    category = models.ForeignKey('Category', on_delete=models.SET_DEFAULT, default=0)
    restaurant_name = models.CharField(max_length = 100)
    restaurant_link = models.CharField(max_length = 500)
    restaurant_content = models.TextField()
    restaurant_address = models.CharField(max_length = 50)
    restaurant_phone = models.CharField(max_length = 40)