from django import forms
from .models import Contact, Quote, NewsLetter


class ContactForm(forms.ModelForm):

	class Meta:
		model = Contact
		fields = "__all__"


class QuoteForm(forms.ModelForm):

	class Meta:
		model = Quote
		fields = "__all__"


class NewsLetterForm(forms.ModelForm):

	class Meta:
		model = NewsLetter
		fields = "__all__"