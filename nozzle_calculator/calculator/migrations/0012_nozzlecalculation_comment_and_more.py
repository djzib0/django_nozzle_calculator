# Generated by Django 4.1 on 2022-10-02 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0011_rename_additionalhours_additionalnozzlehours'),
    ]

    operations = [
        migrations.AddField(
            model_name='nozzlecalculation',
            name='comment',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='nozzlecalculation',
            name='assembly_hours',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='nozzlecalculation',
            name='bending_hours',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='nozzlecalculation',
            name='cutting_plates_hours',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='nozzlecalculation',
            name='medium_machining_hours',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='nozzlecalculation',
            name='rolling_profiles_hours',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='nozzlecalculation',
            name='small_machining_hours',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='nozzlecalculation',
            name='spinning_hours',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='nozzlecalculation',
            name='tos_machining_hours',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='nozzlecalculation',
            name='welding_hours',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]