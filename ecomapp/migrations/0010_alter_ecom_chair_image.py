# Generated by Django 4.0.1 on 2022-02-04 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0009_alter_ecom_chair_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ecom_chair',
            name='image',
            field=models.CharField(default='null', max_length=200),
        ),
    ]
