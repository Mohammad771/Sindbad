# Generated by Django 4.1 on 2023-03-06 20:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stores', '0006_store_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='allowed_seller_numbers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('phone_number', models.CharField(blank=True, max_length=10)),
                ('is_available', models.BooleanField(default=True)),
                ('user_id', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
