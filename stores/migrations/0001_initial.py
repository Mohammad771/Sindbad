# Generated by Django 4.1.4 on 2023-08-11 15:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='allowed_seller_numbers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('phone_number', models.CharField(blank=True, max_length=10, unique=True)),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=24)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=24)),
                ('description', models.TextField()),
                ('link', models.CharField(max_length=300)),
                ('store_photo', models.FileField(blank=True, default=None, null=True, upload_to='static/upload/sellers_stores_photos', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg', 'webp'], message='يمكن رفع الصور فقط بالصيغات التالية: (jpg, png, jpeg, webp')])),
                ('likes', models.IntegerField(default=0)),
                ('categories', models.ManyToManyField(blank=True, related_name='+', to='stores.category')),
            ],
        ),
    ]
