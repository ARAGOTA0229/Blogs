# Generated by Django 4.1.7 on 2023-03-17 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_bloging'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bigslide',
            name='category',
            field=models.CharField(choices=[('Family Law', 'Family Law'), ('Business Law', 'Business Law'), ('Criminal Law', 'Criminal Law')], default='Business Law', max_length=100),
        ),
        migrations.AlterField(
            model_name='slider',
            name='category',
            field=models.CharField(choices=[('Family Law', 'Family Law'), ('Business Law', 'Business Law'), ('Criminal Law', 'Criminal Law')], default='Business Law', max_length=100),
        ),
    ]