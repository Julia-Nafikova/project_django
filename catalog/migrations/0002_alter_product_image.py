# Generated by Django 5.1.2 on 2024-10-23 17:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, help_text='Загрузите изображение товара', null=True,
                                    upload_to='images/', verbose_name='Изображение товара'),
        ),
    ]