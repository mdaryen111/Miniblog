# Generated by Django 4.0.4 on 2023-07-13 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_home_address_home_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
