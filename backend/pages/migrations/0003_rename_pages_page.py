# Generated by Django 5.0.3 on 2024-03-06 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_pages_h1'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pages',
            new_name='Page',
        ),
    ]
