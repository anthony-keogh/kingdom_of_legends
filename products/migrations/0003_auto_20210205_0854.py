# Generated by Django 3.1.3 on 2021-02-05 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='book',
            name='full_book',
            field=models.TextField(default='SOME STRING', max_length=10000),
        ),
    ]