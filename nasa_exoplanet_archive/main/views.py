from django.shortcuts import render
from django.http import HttpResponse
from .models import ExoplanetsData

# Create your views here.
def index(response):
	exoplanets_list = ExoplanetsData.objects.all()

	if response.method == "POST":
		print(response.POST)
		if response.POST.get("sort-by-year-asc"):
			exoplanets_list = ExoplanetsData.objects.order_by("discovery_year")
		elif response.POST.get("sort-by-year-desc"):
			exoplanets_list = ExoplanetsData.objects.order_by("-discovery_year")
		elif response.POST.get("sort-by-light-years-asc"):
			exoplanets_list = ExoplanetsData.objects.order_by("light_years")
		elif response.POST.get("sort-by-light-years-desc"):
			exoplanets_list = ExoplanetsData.objects.order_by("-light_years")
		elif response.POST.get("sort-by-mass-asc"):
			exoplanets_list = ExoplanetsData.objects.order_by("planet_mass")
		elif response.POST.get("sort-by-mass-desc"):
			exoplanets_list = ExoplanetsData.objects.order_by("-planet_mass")
			
	return render(response, "main/index.html", {"exoplanets_list": exoplanets_list})