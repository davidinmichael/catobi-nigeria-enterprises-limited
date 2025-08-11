from django.shortcuts import redirect, render
from django.views import View

from .forms import ContactForm, NewsLetterForm, QuoteForm
from .models import Contact, NewsLetter, Quote



class Home(View):
    def get(self, request):
        return render(request, "core/index.html")

    def post(self, request):
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
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


class Projects(View):
    def get(self, request):
        return render(request, "core/our_projects.html")


class ContactUs(View):
    def get(self, request):
        return render(request, "core/contact.html")

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        return render(request, "core/contact.html")


class RequestQuote(View):
    def get(self, request):
        return render(request, "core/request_quote.html")

    def post(self, request):
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        return render(request, "core/index.html")


class QuotesContacts(View):
    def get(self, request):
        quotes = Quote.objects.all()
        contacts = Contact.objects.all()
        print("Quotes", quotes)
        print("Contacts", contacts)
        return render(request, "core/index.html")


def memo_redirect(request):
    url = "https://netorgft15862178.sharepoint.com/sites/Memo/_layouts/15/listforms.aspx?cid=MzRhNTgwNTAtNjRkOC00NmRkLTkzMmEtMWU1MTM2YmVhOTBk&nav=MWFlMTdkMjYtMjZlZC00NjY3LTg1ZjUtYTJlMzlmNTNiODY0"
    return redirect(url)


