# Generated by Django 5.1.3 on 2024-11-24 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0017_alter_product_status_order_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('RASCUNHO', 'Rascunho'), ('DELETADO', 'Deletado'), ('ESPERAR_APROVACAO', 'Esperar Aprovação'), ('ATIVAR', 'Ativado')], default='Ativado', max_length=50),
        ),
    ]
