from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('portfolio', views.portfolio, name="portfolio"),
    path('contact', views.contact, name="contact"),
    # path('text', views.text, name="staticText"),
    # path('static', views.staticTxtFile, name="staticFile"),
]
