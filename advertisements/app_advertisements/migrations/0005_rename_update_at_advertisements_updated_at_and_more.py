# Generated by Django 4.2.3 on 2023-08-08 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements', '0004_advertisements_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advertisements',
            old_name='update_at',
            new_name='updated_at',
        ),
        migrations.AlterModelTable(
            name='advertisements',
            table=None,
        ),
    ]
