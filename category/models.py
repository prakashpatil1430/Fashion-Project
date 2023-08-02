from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=255, unique=True)
    slug = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=500, blank=True)
    cat_image = models.ImageField(upload_to='photos/categories/', blank=True)

    def __str__(self) -> str:
        return self.category_name