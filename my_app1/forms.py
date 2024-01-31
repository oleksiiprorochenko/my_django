from django import forms


class TeamForm(forms.Form):
    your_team = forms.CharField(label="Your team", max_length=50)

