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

class Services(View):
	def get(self, request, service):
		if service == "valve":
			return render(request, "core/valve.html")
		elif service == "pipeline":
			return render(request, "core/pipeline.html")
		elif service == "training":
			return render(request, "core/training.html")
		elif service == "freight":
			return render(request, "core/freight.html")

class Facilities(View):
	def get(self, request, facility):
		if facility == "testing":
			return render(request, "core/testing_facility.html")
		elif facility == "assembly":
			return render(request, "core/valve_assembly.html")