# Generated by Django 4.1 on 2023-01-09 20:37

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
        ('users', '0007_alter_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.FileField(blank=True, default=None, null=True, upload_to='static/upload/users_photos', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])]),
        ),
        migrations.AddField(
            model_name='user',
            name='store_id',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='stores.store'),
        ),
    ]