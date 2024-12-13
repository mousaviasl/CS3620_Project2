from django import forms

class MadLibForm(forms.Form):
    place = forms.CharField(max_length=100, label="Place")
    adjective = forms.CharField(max_length=100, label="Adjective")
    famous_person = forms.CharField(max_length=100, label="Famous Person")
    noun = forms.CharField(max_length=100, label="Noun")
    verb = forms.CharField(max_length=100, label="Verb")
    plural_noun = forms.CharField(max_length=100, label="Plural Noun")
    number = forms.IntegerField(label="Number")
