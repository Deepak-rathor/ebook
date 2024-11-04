from django.shortcuts import render, get_object_or_404, redirect
from ebookapp.models import Book, Category, SubCategory
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from ebookapp.models import Book
# Create your views here.

def index(request):
    return render(request, 'basicapp/index.html')

def about(request):
    return render(request, "basicapp/about-us.html")

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Signup successful!")
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'basicapp/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                return redirect('index')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'basicapp/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('index')

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'basicapp/category.html', {'categories': categories})

def book_list(request, category_id=None, subcategory_id=None):
    if subcategory_id:
        subcategory = get_object_or_404(SubCategory, id=subcategory_id)
        books = Book.objects.filter(subcategory=subcategory)
        category = subcategory.category
    elif category_id:
        category = get_object_or_404(Category, id=category_id)
        books = Book.objects.filter(category=category)
    else:
        books = Book.objects.all()
        category = None
    return render(request, 'basicapp/book_list.html', {'books': books, 'category': category})


