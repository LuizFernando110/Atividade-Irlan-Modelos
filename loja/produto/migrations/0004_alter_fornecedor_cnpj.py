# Generated by Django 5.1.4 on 2024-12-12 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0003_alter_fornecedor_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fornecedor',
            name='cnpj',
            field=models.CharField(max_length=14, unique=True, verbose_name='CNPJ'),
        ),
    ]
