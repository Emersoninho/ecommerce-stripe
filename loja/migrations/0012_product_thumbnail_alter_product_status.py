# Generated by Django 5.1.3 on 2024-11-23 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0011_alter_product_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/produto_images/thumb_image/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('RASCUNHO', 'Rascunho'), ('ESPERAR_APROVACAO', 'Esperar Aprovação'), ('DELETADO', 'Deletado'), ('ATIVAR', 'Ativado')], default='Ativado', max_length=50),
        ),
    ]
