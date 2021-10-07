from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Weight(models.Model):
    WEIGHT_CHOICES = [
        ("L", "Lightweight"),
        ("M", "Middleweight"),
        ("H", "Heavyweight")
    ]
    # max_length equals 1 to match L, M, H
    weight = models.CharField(
        max_length=1,
        choices=WEIGHT_CHOICES,
        unique=True
    )

    def __str__(self):
        return self.weight


class Character(models.Model):
    name = models.CharField(max_length=30, unique=True)
    image = models.ImageField(blank=True)
    flavor_text = models.CharField(max_length=100, default="They drive fast!")

    weight = models.ForeignKey(to=Weight, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Kart(models.Model):
    def stat_field():
        return models.IntegerField(
            default=1,
            validators=[
                MaxValueValidator(20),
                MinValueValidator(1)
            ]
        )

    name = models.CharField(max_length=30, unique=True)
    image = models.ImageField(blank=True)
    speed = stat_field()
    acceleration = stat_field()
    handling = stat_field()
    drift = stat_field()

    weight = models.ForeignKey(to=Weight, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
