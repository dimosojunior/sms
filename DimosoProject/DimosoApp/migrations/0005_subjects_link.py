# Generated by Django 4.0.3 on 2022-10-10 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DimosoApp', '0004_subjects'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjects',
            name='link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]