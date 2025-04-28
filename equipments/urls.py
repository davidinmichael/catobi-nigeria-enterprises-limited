from django.urls import path
from .views import (
	SandBlastView,
)


urlpatterns = [
	path("sandblast/", SandBlastView.as_view(), name="sandblast"),
]
