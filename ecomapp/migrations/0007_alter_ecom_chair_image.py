# Generated by Django 4.0.1 on 2022-02-03 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0006_alter_ecom_chair_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ecom_chair',
            name='image',
            field=models.ImageField(default='null', max_length=200, upload_to=''),
        ),
    ]