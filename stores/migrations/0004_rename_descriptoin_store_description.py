# Generated by Django 4.1 on 2023-02-04 00:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0003_store_store_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store',
            old_name='descriptoin',
            new_name='description',
        ),
    ]