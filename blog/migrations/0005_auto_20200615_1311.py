# Generated by Django 2.2.12 on 2020-06-15 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200615_1255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='education_experience',
        ),
        migrations.AddField(
            model_name='resume',
            name='education_experience',
            field=models.ManyToManyField(default=1, related_name='employee_education', to='blog.Experience'),
        ),
    ]