from django.shortcuts import render
from .models import Technology
from django.shortcuts import get_object_or_404  

# Create your views here.
tech=Technology.objects.all()
def first(request):
    return render(request, 'app1/first.html' , {'techs': tech})

def detail(request, tech_id):
    techs = get_object_or_404(Technology, id=tech_id)
    return render(request, 'app1/detail.html', {'tech': techs})