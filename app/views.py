from django.shortcuts import render

# Create your views here.
def static_spicific(request):
    return render(request,'h1.html')