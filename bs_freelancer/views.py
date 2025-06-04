from django.shortcuts import render, HttpResponse
import os
import freelancer.settings
from .forms import ContactForm

# Create your views here.

def index(request):
    return render(request, "index.html")

def portfolio(request):
    projects = [
        {"id": "cabinModal","title": "Log Cabin", "img": "img/cabin.png"},
        {"id": "cakeModal","title": "Tasty Cake", "img": "img/cake.png"},
        {"id": "circusModal","title": "Circus Tent", "img": "img/circus.png"},
        {"id": "gameModal", "title": "Controller", "img": "img/game.png"},
        {"id": "safeModal", "title": "Locked Safe", "img": "img/safe.png"},
        {"id": "submarineModal", "title": "Submarine", "img": "img/submarine.png"}
    ]
    return render(request, "portfolio.html", {'projects': projects})

def about(request):
    return render(request, "about.html")

def contact(request):
    success = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            form = ContactForm()  # Clear form after save
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form, 'success': success})



# def text(request):
#     return HttpResponse("Sample message")

# def staticTxtFile(request):
#     file_path = os.path.join(freelancer.settings.BASE_DIR, "static", "test.txt")
#     with open(file_path, "r") as file:
#         content = file.read()
#     return HttpResponse(content, content_type="text/plain")