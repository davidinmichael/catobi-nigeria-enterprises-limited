from django.shortcuts import render
from django.views import View



class Home(View):
	def get(self, request):
		return render(request, "core/index.html")


class CorporateView(View):
	def get(self, request):
		return render(request, "core/corporate_overview.html")
	

class MDDesk(View):
	def get(self, request):
		return render(request, "core/mddesk.html")

class MissionVision(View):
	def get(self, request):
		return render(request, "core/mission.html")
