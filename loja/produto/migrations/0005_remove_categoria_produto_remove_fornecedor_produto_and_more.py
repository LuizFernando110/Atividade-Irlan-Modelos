# Generated by Django 5.1.4 on 2024-12-12 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0004_alter_fornecedor_cnpj'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='produto',
        ),
        migrations.RemoveField(
            model_name='fornecedor',
            name='produto',
        ),
        migrations.AddField(
            model_name='categoria',
            name='produto',
            field=models.ManyToManyField(to='produto.produto'),
        ),
        migrations.AddField(
            model_name='fornecedor',
            name='produto',
            field=models.ManyToManyField(to='produto.produto'),
        ),
    ]
