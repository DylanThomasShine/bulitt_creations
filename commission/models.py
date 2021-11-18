from django.db import models


class Commission(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.first_name
