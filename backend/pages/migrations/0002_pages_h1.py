# Generated by Django 5.0.3 on 2024-03-06 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pages',
            name='h1',
            field=models.TextField(default='test', max_length=100),
            preserve_default=False,
        ),
    ]