# Generated by Django 5.1.3 on 2024-11-22 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0006_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('DELETE', 'Delete'), ('RASCUNHO', 'Rascunho'), ('ATIVAR', 'Ativado'), ('ESPERAR_APROVACAO', 'Esperar Aprovação')], default='ativado', max_length=50),
        ),
    ]