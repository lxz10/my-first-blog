# Generated by Django 2.2.12 on 2020-06-01 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200601_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='images/bitcoin.jpg', upload_to='images/'),
        ),
    ]
