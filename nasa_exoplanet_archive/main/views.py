from django.shortcuts import render
from django.http import HttpResponse
from .models import ExoplanetsData

# Create your views here.
def index(response):
	exoplanets_list = ExoplanetsData.objects.all()
	return render(response, "main/index.html", {"exoplanets_list": exoplanets_list})