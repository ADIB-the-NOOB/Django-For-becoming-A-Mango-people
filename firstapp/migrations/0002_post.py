# Generated by Django 4.0.2 on 2022-04-15 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('salary', models.FloatField()),
                ('details', models.TextField()),
                ('available', models.BooleanField()),
                ('category', models.CharField(choices=[('Teacher', 'Teacher'), ('Student', 'Student')], max_length=100)),
            ],
        ),
    ]
