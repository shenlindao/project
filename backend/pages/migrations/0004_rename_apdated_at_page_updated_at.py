# Generated by Django 5.0.3 on 2024-03-06 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_rename_pages_page'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='apdated_at',
            new_name='updated_at',
        ),
    ]