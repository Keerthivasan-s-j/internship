# Generated by Django 5.0.7 on 2024-07-13 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_feedback_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[(1, 'Electronics'), (2, 'Home'), (3, 'Fashon')], default='Home', max_length=100, verbose_name='Category'),
            preserve_default=False,
        ),
    ]
