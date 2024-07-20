# Generated by Django 5.0.7 on 2024-07-15 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_alter_feedback_ratings'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='prod_category',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='details',
            new_name='prod_details',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='prod_image',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='prod_name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='prod_price',
        ),
        migrations.AlterField(
            model_name='feedback',
            name='ratings',
            field=models.IntegerField(choices=[(1, 'Excelent'), (2, 'Good'), (3, 'Bad')]),
        ),
    ]
