# Generated by Django 4.1 on 2022-09-22 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0003_nozzle_drawing_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nozzle',
            name='inner_ring_type',
            field=models.CharField(choices=[('Complete st. st. inside', 'Wnętrze nierdzewne'), ('St. st. ring inside', 'Pierścień kawitacyjny nierdzewny'), ('Complete steel', 'Wnętrze ze stali zwykłej'), ('St. st. ring and outlet', 'Pierścień kawitacyjny i wylot ze stali nierdzewnej')], max_length=32),
        ),
    ]
