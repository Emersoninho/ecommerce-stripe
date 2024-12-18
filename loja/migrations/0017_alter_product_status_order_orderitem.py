# Generated by Django 5.1.3 on 2024-11-24 14:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0016_alter_product_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('ATIVAR', 'Ativado'), ('ESPERAR_APROVACAO', 'Esperar Aprovação'), ('DELETADO', 'Deletado'), ('RASCUNHO', 'Rascunho')], default='Ativado', max_length=50),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=255)),
                ('s_name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('zip_numero', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('valor_pago', models.IntegerField(blank=True, null=True)),
                ('esta_pago', models.BooleanField(default=False)),
                ('merc_id', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('criado_por', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='loja.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='loja.product')),
            ],
        ),
    ]
