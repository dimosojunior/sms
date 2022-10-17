# Generated by Django 4.0.3 on 2022-04-04 00:29

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('title', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('title_tag', models.CharField(blank=True, max_length=200, null=True)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('source', models.CharField(blank=True, max_length=50, null=True)),
                ('post_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('title_description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='email')),
                ('first_name', models.CharField(max_length=100, verbose_name='first name')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='user name')),
                ('middle_name', models.CharField(max_length=100, verbose_name='middle name')),
                ('last_name', models.CharField(max_length=100, verbose_name='last name')),
                ('company_name', models.CharField(max_length=100, verbose_name='company name')),
                ('phone', models.CharField(max_length=15, verbose_name='phone')),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='get_profile_image_filepath')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('hide_email', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]