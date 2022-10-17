# Generated by Django 4.0.3 on 2022-10-15 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DimosoApp', '0023_alter_marks_average_alter_marks_total_marks'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndividualResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(blank=True, default='ST DIMOSO SEMINARY', max_length=200, null=True)),
                ('kidato', models.CharField(blank=True, default='I', max_length=30, null=True)),
                ('mhula', models.CharField(blank=True, default='I', max_length=30, null=True)),
                ('mwaka', models.CharField(blank=True, default='2022', max_length=30, null=True)),
                ('amekuwa_wa', models.CharField(blank=True, default='5', max_length=30, null=True)),
                ('kati_ya', models.CharField(blank=True, default='200', max_length=30, null=True)),
                ('school_close', models.CharField(blank=True, default='20/11/2022', max_length=50, null=True)),
                ('school_open', models.CharField(blank=True, default='20/01/2022', max_length=50, null=True)),
                ('maoni_ya_mwalimu_wa_darasa', models.TextField(blank=True, max_length=1000, null=True)),
                ('maoni_ya_mkuu_wa_shule', models.TextField(blank=True, max_length=1000, null=True)),
                ('jina_la_mkuu_wa_shule', models.CharField(blank=True, max_length=50, null=True)),
                ('mahitaji', models.TextField(blank=True, max_length=300, null=True)),
                ('maoni_ya_mzazi', models.TextField(blank=True, max_length=300, null=True)),
                ('jina_la_mzazi', models.CharField(blank=True, default='200', max_length=50, null=True)),
                ('tarehe', models.CharField(blank=True, max_length=30, null=True)),
                ('saini', models.CharField(blank=True, max_length=30, null=True)),
                ('alama', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DimosoApp.pangiliaalama')),
                ('results', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DimosoApp.generalresults')),
                ('students', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='DimosoApp.registerstudents')),
                ('tabia', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DimosoApp.importantinformations')),
            ],
            options={
                'verbose_name_plural': 'IndividualResults',
            },
        ),
    ]