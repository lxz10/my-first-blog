# Generated by Django 2.2.12 on 2020-06-17 12:56

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200615_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='resume',
            name='linkedIn',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='resume',
            name='notable_achievements',
            field=models.ManyToManyField(blank=True, default=1, help_text='Includes hackathon participation, online courses and certifications.', related_name='employee_achievements', to='blog.Experience'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='technology_experience',
            field=models.ManyToManyField(default=1, related_name='employee_technology_experience', to='blog.Experience'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('approved_comment', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.Post')),
            ],
        ),
    ]