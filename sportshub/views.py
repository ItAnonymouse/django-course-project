from django.shortcuts import render # type: ignore
from django.http import JsonResponse # type: ignore
import requests # type: ignore

def home(request):
    return render(request, "home.html")

def get_live_scores(request):
    url = "https://sportapi7.p.rapidapi.com/api/v1/sport/football/scheduled-events/2022-02-11"
    headers = {
        "x-rapidapi-key": "748cb84ff1msh5f85f95616276d3p179f03jsnbeef37aa3913",
        "x-rapidapi-host": "sportapi7.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    try:
        data = response.json()
    except ValueError:
        data = {"error": "Invalid JSON"}

    return JsonResponse(data)
