from django.db import models

from .utils import (
    generate_purchase_order,
    generate_tracking_number,
    generate_waybill_number,
)


class Shipment(models.Model):
    client = models.CharField(max_length=100, null=True, blank=True)
    client_email = models.EmailField(null=True, blank=True)
    tracking_number = models.CharField(max_length=50, unique=True, blank=True)
    purchase_order = models.CharField(max_length=50, unique=True, blank=True)
    waybill_number = models.CharField(max_length=50, unique=True, blank=True)
    carrier = models.CharField(max_length=50, null=True, blank=True)
    origin = models.CharField(max_length=100, blank=True, null=True)
    destination = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(
        max_length=100, blank=True, null=True
    )  # e.g., "In Transit", "Delivered"
    last_location = models.CharField(max_length=100, blank=True, null=True)
    estimated_delivery = models.DateField(blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.tracking_number} - {self.get_carrier_display()}"

    def save(self, *args, **kwargs):
        # Auto-generate tracking number if not provided
        if not self.tracking_number:
            tracking = f"CNEL{generate_tracking_number()}"
            while Shipment.objects.filter(tracking_number=tracking).exists():
                tracking = f"CNEL{generate_tracking_number()}"
            self.tracking_number = tracking.upper()
        else:
            self.tracking_number = self.tracking_number.upper()

        if not self.purchase_order:
            purchase_order = f"CNEL{generate_purchase_order()}"
            while Shipment.objects.filter(purchase_order=purchase_order).exists():
                purchase_order = f"CNEL{generate_purchase_order()}"
            self.purchase_order = purchase_order.upper()
        else:
            self.purchase_order = self.purchase_order.upper()

        if not self.waybill_number:
            waybill_number = f"CNEL{generate_waybill_number()}"
            while Shipment.objects.filter(waybill_number=waybill_number).exists():
                tracking = f"CNEL{generate_waybill_number()}"
            self.waybill_number = waybill_number.upper()
        else:
            self.waybill_number = self.waybill_number.upper()

        super().save(*args, **kwargs)


class TrackingEvent(models.Model):
    shipment = models.ForeignKey(
        Shipment, on_delete=models.CASCADE, related_name="events"
    )
    location = models.CharField(max_length=100)
    status_description = models.CharField(max_length=255)  # e.g., "Arrived at facility"
    timestamp = models.DateTimeField()

    class Meta:
        ordering = ["-timestamp"]

    def __str__(self):
        return f"{self.status_description} @ {self.location}"
