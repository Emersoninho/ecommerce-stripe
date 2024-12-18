# Generated by Django 5.1.3 on 2024-11-25 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0018_alter_product_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='merc_id',
            new_name='pagamento_intent',
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('DELETADO', 'Deletado'), ('ATIVAR', 'Ativado'), ('ESPERAR_APROVACAO', 'Esperar Aprovação'), ('RASCUNHO', 'Rascunho')], default='Ativado', max_length=50),
        ),
    ]
