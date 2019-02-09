from django.shortcuts import render
from django.http import HttpResponse

from .models import User,Project,History

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    try:
        user = User.objects.get(pk=1)
    except User.DoesNotExist:
        user = None
    projects = Project.objects.all()
    histories = History.objects.all()
    return render(request, "index.html",{"page":"Home","sandeep": user,"projects":projects,"histories":histories})
    return render(request, "index.html",{"page":"Home","sandeep": user,"projects":projects})

def about(request):
    try:
        user = User.objects.get(pk=1)
    except User.DoesNotExist:
        user = None
    histories = History.objects.all()
    return render(request, "about.html",{"page":"About","sandeep": user,"histories":histories})
    return render(request, "about.html",{"page":"About","sandeep": user})

def portfolio(request):
    try:
        user = User.objects.get(pk=1)
    except User.DoesNotExist:
        user = None
    projects = Project.objects.all()
    return render(request, "portfolio.html",{"page":"Portfolio","sandeep": user,"projects":projects})

def portfolio_detail(request, portfolio_id):
    try:
        user = User.objects.get(pk=1)
    except User.DoesNotExist:
        user = None
    project = Project.objects.get(id=portfolio_id)
    return render(request, "portfolio-details.html",{"page":"Portfolio Detail","sandeep": user,"project":project})


def db(request):
    user = User()
    # User.objects.filter().delete()
    user.name = 'sandeep bangarh'
    user.email = 'sanbangarh309@gmail.com'
    user.phone = '9896747812'
    user.save()

    users = User.objects.all()

    return render(request, "db.html", {"greetings": users})
