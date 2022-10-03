from django.db import models

import datetime

# Create your models here.


class Nozzle(models.Model):
    """Represents Nozzle model"""
    PROFILES = (('Optima', 'Optima'),
                ('19A', '19A'),
                )


    INNER_RING_TYPES = (('Complete st. st. inside', 'Wnętrze nierdzewne'),
                        ('St. st. ring inside', 'Pierścień kawitacyjny nierdzewny'),
                        ('Complete steel', 'Wnętrze ze stali zwykłej'),
                        ('St. st. ring and outlet', 'Pierścień kawitacyjny i wylot ze stali nierdzewnej'))

    date_created = models.DateTimeField(auto_now_add=True)
    diameter = models.PositiveIntegerField(null=False, blank=False)
    profile = models.CharField(max_length=32, choices=PROFILES, null=False, blank=False)
    drawing_number = models.CharField(max_length=32, blank=True)
    profile_height = models.PositiveIntegerField(null=False, blank=False)
    inner_ring_type = models.CharField(max_length=32, choices=INNER_RING_TYPES, null=False, blank=False)
    inner_ring_thickness_propeller_zone = models.PositiveIntegerField(null=False, blank=False)
    inner_ring_thickness_inlet_zone = models.PositiveIntegerField(null=False, blank=False)
    inner_ring_thickness_outlet_zone = models.PositiveIntegerField(null=False, blank=False)
    # if ring thickness in inlet/outlet zone is different than in propeller zone, calculate extra welding seam

    ribs_quantity = models.PositiveIntegerField(null=False, blank=False)
    ribs_thickness = models.PositiveIntegerField(null=False, blank=False)
    segments_quantity = models.PositiveIntegerField(null=False, blank=False)
    segments_thickness = models.PositiveIntegerField(null=False, blank=False)
    has_headbox = models.BooleanField(null=False, blank=False)
    has_outlet_ring = models.BooleanField(null=False, blank=False)
    theoretical_weight = models.PositiveIntegerField(blank=True, default=0)
    real_weight = models.PositiveIntegerField(blank=True, default=0)

    def __str__(self):
        return f"ID: {self.id} - Nozzle {self.diameter} type {self.profile} {self.inner_ring_type}"


class Order(models.Model):
    nozzle = models.ForeignKey(Nozzle, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    order_dmcg_number = models.CharField(max_length=32, blank=False, null=False)
    order_client_number = models.CharField(max_length=32, blank=False, null=False)

    def __str__(self):
        return f"Order {self.order_dmcg_number}/{self.order_client_number}"


class Offer(models.Model):
    this_year = datetime.datetime.now().year

    nozzle = models.ForeignKey(Nozzle, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    dmcg_offer_number = models.CharField(max_length=4, blank=False, null=False)
    client_inquiry_number = models.CharField(max_length=32, blank=True, null=True)
    # offer_client_number = models.CharField(max_length=32, blank=True, null=True)
    offer_year = models.PositiveIntegerField(default=int(this_year), blank=False, null=False)

    def __str__(self):
        return f"Offer {self.dmcg_offer_number}/{self.offer_year} - client number {self.client_inquiry_number}"


class NozzleCalculation(models.Model):
    """Represents calculation for nozzle"""
    nozzle = models.ForeignKey(Nozzle, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    assembly_hours = models.PositiveIntegerField(default=0, blank=True, null=True)
    welding_hours = models.PositiveIntegerField(default=0, blank=True, null=True)
    spinning_hours = models.PositiveIntegerField(default=0, blank=True, null=True)
    small_machining_hours = models.PositiveIntegerField(default=0, blank=True, null=True)
    medium_machining_hours = models.PositiveIntegerField(default=0, blank=True, null=True)
    tos_machining_hours = models.PositiveIntegerField(default=0, blank=True, null=True)
    cutting_plates_hours = models.PositiveIntegerField(default=0, blank=True, null=True)
    bending_hours = models.PositiveIntegerField(default=0, blank=True, null=True)
    rolling_profiles_hours = models.PositiveIntegerField(default=0, blank=True, null=True)
    comment = models.TextField(default='', blank=True, null=True)

    def __str__(self):
        return f'Kalkulacja nr {self.id} - dotyczy dyszy {self.nozzle.id}'


class AdditionalNozzleHours(models.Model):
    """Represents additional hours (if required to be added to calculation"""

    GROUP = [('assembly_hours', 'Montaż'),
             ('welding_hours', 'Spawanie'),
             ('spinning_hours', 'Wyoblanie'),
             ('small_machining_hours', 'Obróbka lekka'),
             ('medium_machining_hours', 'Obróbka średnia'),
             ('tos_machining_hours', 'Obróbka TOS'),
             ('cutting_plates_hours', 'Palenie blach'),
             ('bending_hours', 'Gięcie blach'),
             ('rolling_profiles_hours', 'Walcowanie rur'),
             ]

    calculation = models.ForeignKey(NozzleCalculation, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    additional_hours_amount = models.PositiveIntegerField(default=0, blank=True)
    comment = models.TextField(blank=False, max_length=200)
    group = models.CharField(max_length=40, blank=True, null=True, choices=GROUP)






