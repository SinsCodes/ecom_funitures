# Generated by Django 4.0.1 on 2022-02-02 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0003_admin_reg_customer_reg'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer_reg',
            name='username',
            field=models.CharField(default='null', max_length=200),
            preserve_default=False,
        ),
    ]
