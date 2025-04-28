from django.shortcuts import redirect, render
from django.views import View


class SandBlastView(View):
    
    def get(self, request):
        return render(request, "equipments/sandblast.html")