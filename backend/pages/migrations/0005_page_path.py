# Generated by Django 5.0.3 on 2024-03-06 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_rename_apdated_at_page_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='path',
            field=models.URLField(default='/', max_length=100),
            preserve_default=False,
        ),
    ]
