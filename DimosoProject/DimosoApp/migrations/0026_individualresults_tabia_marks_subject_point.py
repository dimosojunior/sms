# Generated by Django 4.0.3 on 2022-10-16 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DimosoApp', '0025_remove_individualresults_results_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='individualresults',
            name='tabia',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='marks',
            name='subject_point',
            field=models.CharField(blank=True, default='A', max_length=50, null=True),
        ),
    ]
