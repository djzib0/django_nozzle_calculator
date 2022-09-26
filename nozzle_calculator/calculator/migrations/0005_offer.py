# Generated by Django 4.1 on 2022-09-26 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0004_alter_nozzle_inner_ring_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('dmcg_offer_number', models.CharField(max_length=4)),
                ('offer_year', models.PositiveIntegerField(default=2022)),
                ('order_client_number', models.CharField(blank=True, max_length=32, null=True)),
                ('nozzle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator.nozzle')),
            ],
        ),
    ]
