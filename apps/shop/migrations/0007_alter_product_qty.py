# Generated by Django 5.0.7 on 2024-08-29 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='qty',
            field=models.FloatField(default=True, null=True),
        ),
    ]
