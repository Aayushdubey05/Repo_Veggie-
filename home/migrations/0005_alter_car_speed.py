# Generated by Django 5.1.2 on 2024-12-07 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_car_delete_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='speed',
            field=models.IntegerField(default=50),
        ),
    ]
