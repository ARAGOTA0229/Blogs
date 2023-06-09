# Generated by Django 4.1.3 on 2023-03-03 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_stat_alter_bigslide_category_alter_slider_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bigslide',
            name='category',
            field=models.CharField(choices=[('Criminal Law', 'Criminal Law'), ('Business Law', 'Business Law'), ('Family Law', 'Family Law')], default='Business Law', max_length=100),
        ),
        migrations.AlterField(
            model_name='slider',
            name='category',
            field=models.CharField(choices=[('Criminal Law', 'Criminal Law'), ('Business Law', 'Business Law'), ('Family Law', 'Family Law')], default='Business Law', max_length=100),
        ),
        migrations.AlterField(
            model_name='stat',
            name='number',
            field=models.CharField(max_length=1000),
        ),
    ]
