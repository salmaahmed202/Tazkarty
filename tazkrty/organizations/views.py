from django.shortcuts import render
from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Event
from datetime import datetime
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
# from .serializers import UserRegistrationSerializer
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
# from .serializers import UserRegistrationSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from bson.json_util import dumps





# Create your views here.

def insert_event(request):
    if request.method == "POST":
        eventname = request.POST.get("eventname")
        organizer_name = request.POST.get("organizer_name")
        title = request.POST.get("title")
        description = request.POST.get("description")
        date_time = request.POST.get("date_time")
        status = request.POST.get("status")
        location = request.POST.get("location")
        address = request.POST.get("address")
        number_of_seats = request.POST.get("number_of_seats")

        # Convert date_time string to datetime object
        date_time = datetime.strptime(date_time, "%Y-%m-%dT%H:%M")

        # Save to database
        event = Event(
            eventname=eventname,
            organizer_name=organizer_name,
            title=title,
            description=description,
            date_time=date_time,
            status=status,
            location=location,
            address=address,
            number_of_seats=int(number_of_seats)
        )
        event.save()

        return render(request, "organizations/Add_Event.html", {"message": "Event inserted successfully!"})

    return render(request, "organizations/Add_Event.html")



from django.shortcuts import render
from pymongo import MongoClient
from django.conf import settings
client = MongoClient(settings.DATABASES['default']['CLIENT']['host'])
db = client["tazkarty"]  # Your database name
collection = db["bookings"]  # Your collection name

def booking_history(request, email):
    # Fetch all bookings for a specific email
    bookings = list(collection.find({"useremail": email}, {"_id": 0}))  # Exclude _id

    return render(request, 'organizations/history.html', {'bookings': bookings})
