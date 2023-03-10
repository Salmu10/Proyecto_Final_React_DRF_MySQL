from django.db import models

class Category(models.Model):
    slug = models.SlugField(max_length=100, unique=True, editable=False)
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)

class House(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, related_name="category")
    image = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=30, decimal_places=20, null=False)
    longitude = models.DecimalField(max_digits=30, decimal_places=20, null=False)

    def __str__(self):
        return str(self.id)
    
class HouseServices(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE, null=False, related_name="house_services")
    rooms = models.IntegerField()
    bathrooms = models.IntegerField()
    pool = models.BooleanField(default=False)
    wifi = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
