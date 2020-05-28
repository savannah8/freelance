# Generated by Django 2.2.12 on 2020-05-27 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('referralapp', '0020_auto_20200527_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='digital_category',
            field=models.CharField(blank=True, choices=[('Digital Media Marketing', 'I need more traffic to my online business'), ('E-commerce Specialist Required', 'I need an E-commerce Specialist')], max_length=60),
        ),
    ]
