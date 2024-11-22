from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title
    
class Product(models.Model):

    RASCUNHO = 'Rascunho'
    ESPERAR_APROVACAO = 'Esperando Aprovação'
    ATIVAR = 'Ativado'
    DELETADO = 'Deletado'

    STATUS_ESCOLHAS = {
        ('RASCUNHO', 'Rascunho'),
        ('ESPERAR_APROVACAO', 'Esperar Aprovação'),
        ('ATIVAR', 'Ativado'),
        ('DELETADO', 'Deletado'),

    }

    user = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='uploads/produto_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=STATUS_ESCOLHAS, default=ATIVAR)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title
    
    def get_display_price(self):
        return self.price / 100