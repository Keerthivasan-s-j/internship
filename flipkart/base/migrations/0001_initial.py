# Generated by Django 5.0.7 on 2024-07-13 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Product Name')),
                ('image', models.ImageField(upload_to='', verbose_name='Product Image')),
                ('price', models.IntegerField(verbose_name='Product Price')),
                ('discount', models.IntegerField(verbose_name='Discount')),
            ],
        ),
    ]
