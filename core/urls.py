from django.urls import path
from .views import (
	Home, CorporateView, MDDesk, MissionVision, Services, Facilities
)


urlpatterns = [
	path("", Home.as_view(), name="home"),
	path("corporate-overview/", CorporateView.as_view(), name="corporate"),
	path("mddesk/", MDDesk.as_view(), name="mddesk"),
	path("mission/", MissionVision.as_view(), name="mission"),
	path("services/<str:service>/", Services.as_view(), name="services"),
	path("facility/<str:facility>/", Facilities.as_view(), name="facility"),
]
