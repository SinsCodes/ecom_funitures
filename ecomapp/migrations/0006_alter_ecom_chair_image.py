# Generated by Django 4.0.1 on 2022-02-03 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0005_rename_name_admin_reg_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ecom_chair',
            name='image',
            field=models.ImageField(max_length=200, upload_to=''),
        ),
    ]
