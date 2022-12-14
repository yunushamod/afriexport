from django.db import models
from django.conf import settings
from django.urls import reverse
from django.template.defaultfilters import slugify
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['name'])]
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=(self.slug,))

    def __str__(self):
        return self.name

class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, related_name = 'products', on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    quantity = models.IntegerField(default = 0)
    image = models.ImageField(upload_to="products/%Y/%m/%d", blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id','slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created'])
        ]
    def get_absolute_url(self):
        return reverse('shop:product_detail', args=(self.id,self.slug))
    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    # def save(self, *args, **kwargs):
    #     if self.image:
    #         imageTemporary = Image.open(self.image)
    #         outputIOStream = BytesIO()
    #         imageTemporaryResized = imageTemporary.resize((480, 334))
    #         imageTemporaryResized.save(outputIOStream, format='JPEG', quality=85)
    #         outputIOStream.seek(0)
    #         self.image = InMemoryUploadedFile(outputIOStream, 'ImageField', "%s.jpg" % self.image.name.split('.')[0], 'image/jpeg', sys.getsizeof(outputIOStream), None)
    #         super(Product, self).save(*args, **kwargs)
    #     else:
    #         super(Product, self).save()
