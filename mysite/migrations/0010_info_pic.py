# Generated by Django 4.0.2 on 2022-02-28 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0009_info_skils1_info_skils10_info_skils11_info_skils12_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='pic',
            field=models.ImageField(default=1, upload_to='media/'),
            preserve_default=False,
        ),
    ]
