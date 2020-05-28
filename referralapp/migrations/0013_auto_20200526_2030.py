# Generated by Django 2.2.12 on 2020-05-26 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('referralapp', '0012_job_job_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_category',
            field=models.CharField(blank=True, choices=[('Product&Service', 'Products & Services'), ('Software', 'IT & Software'), ('Marketing', 'Marketing & Social Media'), ('Writing', 'Writing & Transcription'), ('Business', 'Business & Customer Service'), ('Referral', 'Agent & Referral'), ('Other', 'Other')], max_length=60),
        ),
    ]
