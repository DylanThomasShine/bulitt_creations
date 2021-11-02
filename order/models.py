from django.db import models


class Order(models.Model):
    name = models.CharField(max_length=254)
    email = models.EmailField()
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
