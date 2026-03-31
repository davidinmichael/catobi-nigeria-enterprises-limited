from django.db import models


class ModeOfTransport(models.TextChoices):
    SEA_FREIGHT = "Sea Freight", "Sea Freight"
    AIR_FREIGHT = "Air Freight", "Air Freight"
    COURIER = "Courier", "Courier"
    PENDING = "Pending", "Pending"
