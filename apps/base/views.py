from django.shortcuts import render
from apps.base.models import Settings,Slide,About,History,Offer,Menu,Team,Experience,Cooking,Clients,Chefs,Gallery,Dessert,Rest,Dinner

# Create your views here.
def index(request):
    settings = Settings.objects.latest('id')
    slide = Slide.objects.all()
    about = About.objects.latest("id")
    history = History.objects.latest("id")
    offer = Offer.objects.all()
    menu = Menu.objects.all()
    team = Team.objects.all()
    experience = Experience.objects.latest("id")
    cooking = Cooking.objects.latest("id")
    clients = Clients.objects.latest("id")
    chefs = Chefs.objects.latest("id")
    gallery = Gallery.objects.all()
    dessert = Dessert.objects.all()
    restuarant = Rest.objects.all()
    dinner = Dinner.objects.all()

    return render(request,'index.html', locals())