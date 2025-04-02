import os
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from articles.models import Content
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from articles.forms import ContentForm


def home_view(request):
    content = Content.objects.all()
    context = {
        "contents": content
    }
    return render(request, 'index.html', context)

def detail_view(request, content_id):
    content_obj = Content.objects.get(pk=content_id)
    context = {
        "content": content_obj,
    }
    return render(request, 'details.html', context=context)

def search_view(request):
    query = request.GET.get('query', '')

    query_results = Content.objects.filter(
        Q(title__icontains=query) |
        Q(content__icontains=query) |
        Q(author__icontains=query)
    ) if query else None

    context = {
        'query': query,
        'contents': query_results
    }
    return render(request, 'search.html', context=context)


@login_required
def create_view(request):
    if request.method == 'POST':
        form = ContentForm(request.POST)
        if form.is_valid():
            content = form.save(commit=False)  # Don't save yet
            content.author = request.user.username  # Set author automatically
            content.save()  # Now save
            return redirect('home')
    else:
        form = ContentForm()

    return render(request, 'create.html', {'form': form})


# Login View
def login_view(request):
    next_url = request.GET.get('next')  # Get next URL from GET request (when arriving at login page)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next', 'home')  # Get next URL from POST request (after login)
            return redirect(next_url)  # Redirect to 'next' or home
        else:
            messages.error(request, "Invalid credentials")
    
    return render(request, 'login.html', {'next': next_url})

# Account View
def account_view(request):
    active_tab = request.GET.get('tab', 'personal')  # Default to 'personal'
    
    context = {
        'active_tab': active_tab,
        'user': request.user  # Pass the current user object to the template
    }
    
    return render(request, 'account.html', context)


# Signup View
def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, "Account created successfully!")
            return redirect('login')  # Redirect to login page after signup
    return render(request, 'signup.html')

# Logout View
def logout_view(request):
    logout(request)
    return redirect('login')


def robots_txt(request):
    robots_path = os.path.join(settings.BASE_DIR, "robots.txt")
    
    try:
        with open(robots_path, "r") as file:
            content = file.read()
        return HttpResponse(content, content_type="text/plain")
    except FileNotFoundError:
        return HttpResponse("User-agent: *\nDisallow: /", content_type="text/plain")