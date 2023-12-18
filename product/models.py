from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
# Create your models here.

User = settings.AUTH_USER_MODEL

class Product(models.Model):
    STATUS = (
        ("Available", "Available"),
        ("Uavailable", "Unavailable")
    )
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='user')
    name = models.CharField(_('Enter product name'), max_length=100)
    image = models.ImageField(upload_to='media/product')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quantity = models.IntegerField(default=0)
    stock = models.CharField(choices=STATUS, default='available', max_length=100)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products',
                                 null=True,
                                 blank=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [ 
            models.Index(fields=['-created'])
        ]
        ordering = ['-created']

    def __str__(self):
        return self.name
