from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    neighbourhood = Neighbourhood.objects.all()
    context = {
    'neighbourhood': neighbourhood,
    }
    return render(request, 'index.html', context)