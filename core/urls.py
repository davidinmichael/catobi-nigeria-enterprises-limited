from django.urls import path
from .views import (
	Home, CorporateView, MDDesk, MissionVision
)


urlpatterns = [
	path("", Home.as_view(), name="home"),
	path("corporate-overview/", CorporateView.as_view(), name="corporate"),
	path("mddesk/", MDDesk.as_view(), name="mddesk"),
	path("mission/", MissionVision.as_view(), name="mission"),
]
