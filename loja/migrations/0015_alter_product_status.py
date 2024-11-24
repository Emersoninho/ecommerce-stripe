# Generated by Django 5.1.3 on 2024-11-23 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0014_alter_product_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('ESPERAR_APROVACAO', 'Esperar Aprovação'), ('RASCUNHO', 'Rascunho'), ('ATIVAR', 'Ativado'), ('DELETADO', 'Deletado')], default='Ativado', max_length=50),
        ),
    ]