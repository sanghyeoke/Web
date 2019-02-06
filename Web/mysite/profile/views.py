from django.shortcuts import render
from django.http import HttpResponse

from .models import MainProfile

# Create your views here.
def index(reqeust):
    mainProfile = MainProfile.objects.all()
    context = {'mainProfile':mainProfile}
    return render(reqeust, 'profile/index.html', context)
