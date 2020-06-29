from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dir = {'connect_me':'This is from Template Folder'}
    return render(request, 'first_app/index.html', my_dir)
