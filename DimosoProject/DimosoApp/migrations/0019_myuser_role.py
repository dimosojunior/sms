# Generated by Django 4.0.3 on 2022-10-15 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DimosoApp', '0018_pangiliaalama'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='role',
            field=models.CharField(choices=[('ADMIN TEACHER', 'ADMIN TEACHER'), ('STAFF TEACHER', 'STAFF TEACHER'), ('MULTI TEACHER', 'MULTI TEACHER'), ('PHYSICS TEACHER', 'PHYSICS TEACHER'), ('CHEMISTRY TEACHER', 'CHEMISTRY TEACHER'), ('BIOLOGY TEACHER', 'BIOLOGY TEACHER'), ('ENGLISH TEACHER', 'ENGLISH TEACHER'), ('CIVICS TEACHER', 'CIVICS TEACHER'), ('MATHEMATICS TEACHER', 'MATHEMATICS TEACHER'), ('HISTORY TEACHER', 'HISTORY TEACHER'), ('GEOGRAPHY TEACHER', 'GEOGRAPHY TEACHER'), ('KISWAHILI TEACHER', 'KISWAHILI TEACHER')], default=0, max_length=50, verbose_name='role'),
            preserve_default=False,
        ),
    ]
