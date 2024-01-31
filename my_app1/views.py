from django.shortcuts import render

from django.http import HttpResponse
from .models import Person
from .forms import TeamForm


def index(request):
    return render(request, 'main.html')

def header_footer (request):
    return render (request, 'header_footer.html')

def return_simple_html(request): 

    blog_city = {"Kyiv": "Ukraine", "Berlin": "Germany", "Rome": "Italy"}

    return render(request, 'child.html', context={"blog_city": blog_city})

def css_style(request):
    list_of_teams = [{"city": "Kyiv", "team": "Dynamo"},
                    {"city": "Berlin", "team": "Hertha"},
                    {"city": "Rome", "team": "Lazio"}]
    
    return render (request, 'html_for_css.html', context={"list_of_teams": list_of_teams})

def get_team(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = TeamForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TeamForm()

    return render(request, "header_footer.html", {"form": form})



