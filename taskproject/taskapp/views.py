from django.shortcuts import render
from django.http import HttpResponse

from.models import jithin
from.models import inmakes

# Create your views here.
def voice(request):
    jit=jithin.objects.all()
    car=inmakes.objects.all()
    return render(request, "index.html", {'balan':jit , 'y':car})




