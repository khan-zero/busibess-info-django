# Generated by Django 4.2.11 on 2024-09-30 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_info', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourservice',
            name='icon',
            field=models.ImageField(upload_to=''),
        ),
    ]
