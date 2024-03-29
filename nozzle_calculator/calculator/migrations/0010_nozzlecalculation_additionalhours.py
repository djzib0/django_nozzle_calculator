# Generated by Django 4.1 on 2022-09-30 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0009_remove_offer_offer_client_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='NozzleCalculation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('assembly_hours', models.PositiveIntegerField(blank=True, null=True)),
                ('welding_hours', models.PositiveIntegerField(blank=True, null=True)),
                ('spinning_hours', models.PositiveIntegerField(blank=True, null=True)),
                ('small_machining_hours', models.PositiveIntegerField(blank=True, null=True)),
                ('medium_machining_hours', models.PositiveIntegerField(blank=True, null=True)),
                ('tos_machining_hours', models.PositiveIntegerField(blank=True, null=True)),
                ('cutting_plates_hours', models.PositiveIntegerField(blank=True, null=True)),
                ('bending_hours', models.PositiveIntegerField(blank=True, null=True)),
                ('rolling_profiles_hours', models.PositiveIntegerField(blank=True, null=True)),
                ('nozzle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator.nozzle')),
            ],
        ),
        migrations.CreateModel(
            name='AdditionalHours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('additional_hours_amount', models.PositiveIntegerField(blank=True, default=0)),
                ('comment', models.TextField()),
                ('calculation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator.nozzlecalculation')),
            ],
        ),
    ]
