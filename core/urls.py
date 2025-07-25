from django.urls import path
from django.http import HttpResponse
from .views import (
	Home, CorporateView, MDDesk, MissionVision, Services, Facilities, Projects, ContactUs, QuotesContacts, RequestQuote
)
from . import views


urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("corporate-overview/", CorporateView.as_view(), name="corporate"),
    path("mddesk/", MDDesk.as_view(), name="mddesk"),
    path("mission/", MissionVision.as_view(), name="mission"),
    path("services/<str:service>/", Services.as_view(), name="services"),
    path("facility/<str:facility>/", Facilities.as_view(), name="facility"),
    path("projects/", Projects.as_view(), name="projects"),
    path("contact-us/", ContactUs.as_view(), name="contact"),
    path("request-a-quote/", RequestQuote.as_view(), name="quote"),
    path("leads/", QuotesContacts.as_view(), name="leads"),
]
