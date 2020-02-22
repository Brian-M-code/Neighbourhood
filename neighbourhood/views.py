from django.shortcuts import render, redirect
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

class NeighbourhoodListView(ListView):
    model = Neighbourhood
    template_name = 'neighbour_list.html'
    
    if request.method == 'POST':
        if form.is_valid:
            post = form.save(commit=False)
            post.user = current_user
            post.post = post
            post.post_id = post.id
            post.save()
            return redirect('index')
    
    else:
        post = PostForm()
        
    return render (request, 'post.html', {'form':form, 'neighbourhood':neighbourhood, 'business':business})