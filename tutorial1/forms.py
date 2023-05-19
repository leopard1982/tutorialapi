from django import forms


class inputUser(forms.Form):
	username = forms.CharField(max_length=200)
	email= forms.CharField(max_length=200)