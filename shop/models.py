from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,
    unique=True,blank=True)
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    def __str__(self):
        return self.name
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        super(Category,self).save(*args, **kwargs)

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name ='products')
    name = models.CharField(max_length = 200)
    slug = models.SlugField(max_length = 200,blank=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    discription = models.TextField(blank=True)
    price = models.DecimalField( max_digits=10, decimal_places=2) 
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    

    def nom_of_ratings(self):
        ratings = Rating.objects.filter(product=self)
        return len(ratings)
    
    def avg_rating(self):
        sum = 0
        ratings = Rating.objects.filter(product=self)
        for rate in ratings:
            sum += rate.stars
        if len(ratings) > 0:

            return sum / len(ratings)
        else:
            return 0


    class Meta:
        ordering = ['name']
        indexes = [
        models.Index(fields=['id', 'slug']),
        models.Index(fields=['name']),
        models.Index(fields=['-created']),
        ]
    def __str__(self):
        return self.name
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        super(Product,self).save(*args, **kwargs)


class Rating(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    def __str__(self) -> str:
        return str(f"  User : {self.user} | Product : {self.product}  |   Stars : {self.stars}")
    
    class Meta:
        unique_together = (('user','product'),)
        index_together = (('user','product'),)


class ProductComments(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name = 'product_comments')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)