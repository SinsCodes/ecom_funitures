# Generated by Django 4.0.1 on 2022-02-10 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0012_alter_ecom_dining_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ecom_Bed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
                ('discount', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('image', models.ImageField(default='null', upload_to='')),
            ],
        ),
    ]
