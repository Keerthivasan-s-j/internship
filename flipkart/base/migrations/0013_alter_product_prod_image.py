# Generated by Django 5.0.7 on 2024-07-16 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_alter_product_seller_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='prod_image',
            field=models.ImageField(upload_to='images/', verbose_name='Product Image'),
        ),
    ]
