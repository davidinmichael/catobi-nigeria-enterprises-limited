from django.urls import path
from .views import (
	Home, CorporateView,
)


urlpatterns = [
	path("", Home.as_view(), name="home"),
	path("corporate-overview/", CorporateView.as_view(), name="corporate"),
]
