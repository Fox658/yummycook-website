from django.shortcuts import render 
from tutoriales.models import SerieTutoriales

def homepage(request):
    series = SerieTutoriales.objects.all()
    return render(request,'homepage.html', {'series':series})
    
def about(request):
    return render(request,'about.html')