from django.db import models
from django.utils.translation import gettext_lazy as _


class Services(models.TextChoices):
	FREIGHT = "freight", _("Freight")
	VALVE = "valve_maintenance", _("Valve Maintenance")
	PROCUREMENT = "valve_procurement", _("Valve Procurement")
	PIPELINE = "pipeline", _("Pipeline")
	BLASTING = "blasting", _("Blasting")
	TRAINING = "training", _("Training")
	OTHER = "other", _("Other")

class Contact(models.Model):
	name = models.CharField(max_length=50, null=True, blank=True)
	email = models.EmailField()
	subject = models.CharField(max_length=100, null=True, blank=True)
	message = models.TextField()

	def __str__(self):
		return f"{self.name} | {self.subject}"
	

class Quote(models.Model):
	name = models.CharField(max_length=50, null=True, blank=True)
	email = models.EmailField()
	phone = models.CharField(max_length=20, null=True, blank=True)
	service = models.CharField(max_length=20, null=True, blank=True, choices=Services.choices)
	message = models.TextField()

	def __str__(self):
		return f"{self.name} | {self.service}"


class NewsLetter(models.Model):
	email = models.EmailField()

	def __str__(self):
		return self.email