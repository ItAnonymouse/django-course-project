import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings

# Home page view to show "Welcome to SportsHub!" and the football events
def home(request):
    return render(request, "home.html", {"message": "Welcome to SportsHub!"})

# API view to get scheduled football events
def get_scheduled_football_events(request, date):
    try:
        url = f"https://sportapi7.p.rapidapi.com/api/v1/sport/football/scheduled-events/{date}"
        headers = {
            "x-rapidapi-key": "748cb84ff1msh5f85f95616276d3p179f03jsnbeef37aa3913",
            "x-rapidapi-host": "sportapi7.p.rapidapi.com"
        }
        
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise error for bad responses
        
        events = response.json().get("events", [])
        
        # Render the events on the same page if required
        return render(request, "home.html", {"message": "Welcome to SportsHub!", "events": events})
        
    except requests.RequestException as e:
        return JsonResponse({"error": str(e)}, status=500)
