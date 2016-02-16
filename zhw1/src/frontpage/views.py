from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    all_objects= blog.objects.all()
    first_object= all_objects[0]
    title_first_object= first_object.title 
    template="home.html" 
    context={
        "all_objects": all_objects,
        "first_object": first_object, 
    }
    return render(request,template,context)
