# Generated by Django 4.1.3 on 2023-03-15 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_bigslide_category_alter_comments_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bloging',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=400)),
                ('photo', models.ImageField(upload_to='media/blog')),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('views', models.IntegerField()),
                ('like', models.IntegerField()),
            ],
        ),
    ]
