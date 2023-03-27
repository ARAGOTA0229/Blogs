# Generated by Django 4.1.3 on 2023-03-03 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_bigphoto_bigslide_alter_slider_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('text', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='bigslide',
            name='category',
            field=models.CharField(choices=[('Criminal Law', 'Criminal Law'), ('Family Law', 'Family Law'), ('Business Law', 'Business Law')], default='Business Law', max_length=100),
        ),
        migrations.AlterField(
            model_name='slider',
            name='category',
            field=models.CharField(choices=[('Criminal Law', 'Criminal Law'), ('Family Law', 'Family Law'), ('Business Law', 'Business Law')], default='Business Law', max_length=100),
        ),
    ]