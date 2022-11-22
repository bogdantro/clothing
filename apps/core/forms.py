from django import forms

class ContactForm(forms.Form):
    fra_epost = forms.CharField(required=True)
    grunn = forms.CharField(required=True)
    beskjed = forms.CharField(widget=forms.Textarea, required=True)

class HelpForm(forms.Form):
    fra_epost = forms.EmailField(required=True)
    hud_type = forms.CharField(required=True)
    alder = forms.IntegerField(required=True, min_value=0)
    kjønn = forms.CharField(required=True)
