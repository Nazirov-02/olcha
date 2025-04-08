from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Category(BaseModel):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.name

class Section(BaseModel):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='sections')
    def __str__(self):
        return self.name

class Product(BaseModel):
    section = models.ForeignKey(Section, on_delete=models.CASCADE,related_name='products')
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField(default=1)
    def __str__(self):
        return self.name

class Comment(BaseModel):
    class Rating(models.IntegerChoices):
        One = 1, 'One'
        Two = 2, 'Two'
        Three = 3, 'Three'
        Four = 4, 'Four'
        Five = 5, 'Five'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')  # Foydalanuvchi bilan bog‘lanadi
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    rating = models.PositiveIntegerField(choices=Rating.choices, default=Rating.One)
    def __str__(self):
        return self.user.username


class Image(BaseModel):
    image = models.ImageField(upload_to='images/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='images')
    def __str__(self):
        return self.product.name

class Characteristic(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='characteristics')
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    def __str__(self):
        return self.name,self.value