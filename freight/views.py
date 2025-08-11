import os

import requests
from bs4 import BeautifulSoup
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from dotenv import load_dotenv

from .forms import ShipmentForm, TrackingEventForm
from .models import Shipment, TrackingEvent

load_dotenv()

DHL_BASE_URL = os.getenv("DHL_BASE_URL")
DHL_API_KEY = os.getenv("DHL_API_KEY")


class CreateShipment(View):
    def get(self, request):
        return render(request, "freight/shipment.html")

    def post(self, request):
        forms = ShipmentForm(data=request.POST)
        if forms.is_valid():
            shipment = forms.save()
            return redirect("shipment_details", pk=shipment.pk)
        return render(request, "freight/shipment.html")


def view_shipments(request):
    shipments = Shipment.objects.all()
    return render(request, "freight/all_shipments.html", {"shipments": shipments})


def shipment_detail(request, pk):
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
            return redirect("freight")
        events = shipment_ob.events.all()

        context = {
            "shipment": shipment_ob,
            "events": events,
        }
        return render(request, "freight/track_results.html", context)
