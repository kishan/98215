from django.shortcuts import render
from .models import *

from .forms import BlogPosts 


# Create your views here.
def home(request):
    all_objects= blog.objects.all()
    first_object= all_objects[0]
    title_first_object= first_object.title 

    template="home.html" 

    form = BlogPosts(request.POST or None)

    if form.is_valid():
        variable = form.save(commit='false')
        variable.save() 

    context={
    	"form": form,
        "all_objects": all_objects,
        "first_object": first_object, 
    }
    return render(request,template,context)
