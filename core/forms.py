from django import forms
from .models import Contact, Quote


class ContactForm(forms.ModelForm):

	class Meta:
		model = Contact
		fields = "__all__"


class QuoteForm(forms.ModelForm):

	class Meta:
		model = Quote
		fields = "__all__"