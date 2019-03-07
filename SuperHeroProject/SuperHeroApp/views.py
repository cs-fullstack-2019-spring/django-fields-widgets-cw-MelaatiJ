from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import SuperHeroModel
from .forms import SuperHeroForm


# index view to render to index page
def index(request):
    return render(request, "SuperHeroApp/index.html", )

# welcome view with form that saves the data
def welcome(request):
    form = SuperHeroForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('thankYou')
    return render(request, "SuperHeroApp/welcome.html", {"form": form})


# thanks the applicants
def thankYou(request):
    return render(request, "SuperHeroApp/thankYou.html")
