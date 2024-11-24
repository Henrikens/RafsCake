# Generated by Django 4.2.4 on 2023-09-12 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('ProdutoCodigo', models.IntegerField(primary_key=True, serialize=False)),
                ('ProdutoNome', models.CharField(max_length=255)),
                ('ProdutoDescricao', models.CharField(max_length=255)),
                ('ProdutoValor', models.FloatField()),
                ('ProdutoImagem', models.ImageField(upload_to='produtos/')),
            ],
        ),
    ]