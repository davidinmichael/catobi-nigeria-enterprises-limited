import os

import requests
from bs4 import BeautifulSoup
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.views import View
from dotenv import load_dotenv

from core.utils import send_email

from .forms import ShipmentForm, TrackingEventForm
from .models import Shipment, TrackingEvent

load_dotenv()

DHL_BASE_URL = os.getenv("DHL_BASE_URL")
DHL_API_KEY = os.getenv("DHL_API_KEY")
BASE_URL = os.getenv("BASE_URL")


class CreateShipment(View):
    def get(self, request):
        if not request.user.is_authenticated:
            messages.error(request, "Only accessible to Admins.")
            return redirect("login")
        return render(request, "freight/shipment.html")

    def post(self, request):
        if not request.user.is_authenticated:
            messages.error(request, "Only accessible to Admins.")
            return redirect("login")
        forms = ShipmentForm(data=request.POST)
        if forms.is_valid():
            shipment = forms.save()
            email = shipment.client_email
            context = {
                "client_email": email,
                "shipment": shipment,
                "url": f"{BASE_URL}/freight/track-courier/?tracking_number={shipment.tracking_number}",
            }
            template = render_to_string("freight/shipment_email.html", context)
            print("Calling email function")
            send_email(email, "Catobi Freight: Shipment Status", template)
            messages.success(request, "Shipment successfully added!")
            return redirect("shipment_details", pk=shipment.pk)
        messages.error(request, "Error! Confirm the details and try again.")
        print(f"Errors: {forms.errors}")
        return render(request, "freight/shipment.html")


def view_shipments(request):
    if not request.user.is_authenticated:
        messages.error(request, "Only accessible to Admins.")
        return redirect("login")
    shipments = Shipment.objects.all()
    return render(request, "freight/all_shipments.html", {"shipments": shipments})


def shipment_detail(request, pk):
    if not request.user.is_authenticated:
        messages.error(request, "Only accessible to Admins.")
        return redirect("login")
    shipment = get_object_or_404(Shipment, pk=pk)
    events = shipment.events.all()  # Because of related_name="events"

    if request.method == "POST":
        form = TrackingEventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.shipment = shipment
            event.save()

            # Update shipment fields based on event
            shipment.last_location = event.location
            shipment.status = event.status_description
            shipment.save()

            email = shipment.client_email
            print(f"Email: {email}")
            context = {
                "client_email": email,
                "shipment": shipment,
                "url": f"{BASE_URL}/freight/track-courier/?tracking_number={shipment.tracking_number}",
            }
            template = render_to_string("freight/shipment_update.html", context)
            send_email(email, "Catobi Freight: Shipment Update", template)

            return redirect("shipment_details", pk=shipment.pk)
    else:
        form = TrackingEventForm()

    return render(
        request,
        "freight/shipment_detail.html",
        {
            "shipment": shipment,
            "events": events,
            "form": form,
        },
    )


def freight_view(request):
    return render(request, "freight/freight.html")


class TrackShipments(View):
    def get(self, request):
        tracking_number = request.GET.get("tracking_number")
        if not tracking_number:
            return redirect("freight")
        print(f"Tracking: {tracking_number}")
        try:
            shipment_ob = Shipment.objects.get(
                tracking_number=tracking_number.strip().upper()
            )
        except Shipment.DoesNotExist:
            messages.error(
                request,
                f"Shipment with ID '{tracking_number.strip().upper()}' not found, confirm the tracking number and try again!",
            )
            return redirect("freight")
        events = shipment_ob.events.all()

        context = {
            "shipment": shipment_ob,
            "events": events,
        }
        return render(request, "freight/track_results.html", context)
