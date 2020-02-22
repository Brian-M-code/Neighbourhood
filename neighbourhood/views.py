from django.shortcuts import render, redirect

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

def neighbourhood(request, pk):
    current_user = request.user
    neighbourhood = Neighbourhood.objects.get(pk=pk)
    business = Business.get_business(business.id)
    form = PostForm(request.Post)
    
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