# Generated by Django 4.0.3 on 2022-10-10 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DimosoApp', '0002_activities_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterStudents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regno', models.IntegerField(unique=True)),
                ('first_name', models.CharField(max_length=200)),
                ('middle_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=30, unique=True)),
                ('gender', models.CharField(blank=True, choices=[('', 'Choose Gender'), ('Male', 'Male'), ('Female', 'Female')], max_length=7, null=True)),
                ('recorded_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='StudentsImages/')),
                ('phone', models.CharField(max_length=13)),
            ],
            options={
                'verbose_name_plural': 'RegisterStudents',
            },
        ),
    ]
