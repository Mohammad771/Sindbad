# Generated by Django 4.1 on 2023-03-08 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0007_allowed_seller_numbers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allowed_seller_numbers',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10, unique=True),
        ),
    ]
