from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=190)
    image = models.ImageField(upload_to='image')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=190)
    image = models.ImageField(upload_to='image')
    price = models.FloatField()
    category = models.ForeignKey(Category, related_name="category",  on_delete=models.CASCADE)
    description = models.TextField(null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
