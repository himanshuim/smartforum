#from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from .models import Blog, Rank, Login, Profile_info
from .forms import BlogForm

def home_page(request):
    return render(request, 'index.html')

def log_out(request):
    logout(request)
    return redirect('/')
        


def login(request):
    return render(request, 'login.html')
def register(request):
    return render(request, 'register.html')
def profile(request):
    profile_value = Profile_info.objects.all()[0]
    blog = Blog.objects.all()
    context = {
        'profile_value': profile_value,
        'blog': blog
    }
    return render(request, 'profile.html', context)    
def blog(request):
    form = BlogForm()
    blog = Blog.objects.all()
    context = {
        'form': form,
        'blog': blog
    }
    if request.method == 'POST':
        form = BlogForm(request.POST or None)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            message = form.cleaned_data.get('message')
            blogs = Blog(title=title, message=message)
            blogs.save()        
            #  return redirect('/')
        else:
            print('Error')
            # message = request.POST.get('message', '')
            # blogs = Blog(title=title, message=message)
            # blogs.save()       
            # return redirect('')
            # return render(request, 'blog.html',{'blog': blog})
            # items_json = request.POST.get('itemsJson', '')     
        # thank = True
        # id = order.order_id
        #  return render(request, 'blog.html',{'blog': blog})
    return render(request, 'blog.html', context)
def rank(request):
    rank_value = Rank.objects.all()
    return render(request, 'rank.html',{'rank_value': rank_value}) 

# def profile_info(request):
#     profile_value = Profile_info.objects.all()[0]
#     print('######')
#     print(profile_value)
#     return render(request, 'profile.html',{'profile_value': profile_value}) 
    
    
