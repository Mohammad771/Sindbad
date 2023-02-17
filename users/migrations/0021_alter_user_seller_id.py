# Generated by Django 4.1 on 2023-02-13 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_user_liked_stores'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='seller_id',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='users.seller'),
        ),
    ]