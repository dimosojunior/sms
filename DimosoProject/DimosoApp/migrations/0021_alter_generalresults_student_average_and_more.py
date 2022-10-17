# Generated by Django 4.0.3 on 2022-10-15 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DimosoApp', '0020_alter_generalresults_student_average_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalresults',
            name='student_average',
            field=models.DecimalField(blank=True, decimal_places=3, default=0.0, max_digits=100, null=True),
        ),
        migrations.AlterField(
            model_name='marks',
            name='Average',
            field=models.DecimalField(blank=True, decimal_places=3, default=0.0, max_digits=100, null=True),
        ),
    ]