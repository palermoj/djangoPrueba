from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120) #max length is required
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    #summary = models.TextField()

    def get_absolute_url(self):
        return f"/product/{self.id}/"

