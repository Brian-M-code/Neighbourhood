from django.shortcuts import render, redirect
from django.http  import HttpResponse
from django.views.generic import ListView
from .models import Neighbourhood

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def index(request):
    neighbourhood = Neighbourhood.objects.all()
    context = {
    'neighbourhood': neighbourhood,
    }
    return render(request, 'index.html', context,{"neighbourhood":neighbourhood})

def profile(request):
    date = dt.date.today()
    current_user = request.user
    profile = Profile.objects.get(user=current_user.id)
    hoods = Neighbourhood.objects.all()
    return render(request, 'profile/profile.html', {"date": date, "profile":profile,"hoods":hoods})
def edit_profile(request):
    date = dt.date.today()
    current_user = request.user
    profile = Profile.objects.get(user=current_user.id)
    if request.method == 'POST':
        signup_form = EditForm(request.POST, request.FILES,instance=request.user.profile)
        if signup_form.is_valid():
            signup_form.save()
            return redirect('profile')
    else:
        signup_form =EditForm()
    return render(request, 'profile/edit_profile.html', {"date": date, "form":signup_form,"profile":profile})

def search_results(request):
    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_businesses = Business.objects.filter(name=search_term)
        message = f"{search_term}"
        profiles=  Profile.objects.all( )
        return render(request, 'search.html',{"message":message,"business": searched_businesses,'profiles':profiles})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})


class NeighbourhoodListView(ListView):
    model = Neighbourhood
    template_name = 'neighbour_list.html'
    
   