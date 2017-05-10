from django import forms


class NameForm (forms.Form):
    your_name = forms.CharField(label="Your Name", max_length=100)

class ContactForm (forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    email = forms.CharField(label= "Email", max_length= 100)
    question = forms.CharField(label= "Question", max_length= 500)
