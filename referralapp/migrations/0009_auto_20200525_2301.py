# Generated by Django 2.2.12 on 2020-05-25 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('referralapp', '0008_auto_20200525_2200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='token',
            name='token_price',
        ),
        migrations.DeleteModel(
            name='ConfirmPayment',
        ),
    ]
