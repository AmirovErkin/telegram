from django.shortcuts import render
from . import models
# Create your views here.
def index(request):
    return render(request, 'tele/index.html', {'posts': models.tele_class.objects.all()})

