from django.db import models

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
        return f"Nozzle {self.diameter} type {self.profile} {self.inner_ring_type}"


class Order(models.Model):
    nozzle = models.ForeignKey(Nozzle, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    order_dmcg_number = models.CharField(max_length=32, blank=False, null=False)
    order_client_number = models.CharField(max_length=32, blank=False, null=False)

    def __str__(self):
        return f"Order {self.order_dmcg_number}/{self.order_client_number}"
