# Generated by Django 4.0.3 on 2022-10-13 18:53

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DimosoApp', '0012_alter_generalresults_students'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImportantInformations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habit', models.CharField(blank=True, choices=[(' ', "Fill Student's Behaviour"), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F')], max_length=200, null=True)),
                ('debt', models.BooleanField(blank=True, default='False', null=True)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('students', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='DimosoApp.registerstudents')),
            ],
            options={
                'verbose_name_plural': 'ImportantInformations',
            },
        ),
    ]
