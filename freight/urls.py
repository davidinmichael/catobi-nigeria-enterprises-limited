from django.urls import path

from . import views
from .views import CreateShipment, TrackShipments, EditShipmentView

urlpatterns = [
    path("", views.freight_view, name="freight"),
    path("track-courier/", TrackShipments.as_view(), name="track_courier"),
    path(
        "admin-freight/create-shipment/",
        CreateShipment.as_view(),
        name="create_shipment",
    ),
    path("admin-freight/all-shipments/", views.view_shipments, name="view_shipments"),
    path(
        "admin-freight/shipment-details/<int:pk>/",
        views.shipment_detail,
        name="shipment_details",
    ),
    path(
        "admin-freight/delete-shipment/<int:pk>/",
        EditShipmentView.as_view(),
        name="delete_shipment",
    ),
]
