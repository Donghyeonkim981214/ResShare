from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from users import models as user_models
from shareRes import models as res_models

# Create your models here.
class Review(models.Model):
    review = models.TextField()
    created_by = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(res_models.Restaurant, on_delete=models.CASCADE)
    postedDay = models.DateTimeField(auto_now_add = True)
    rate = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )