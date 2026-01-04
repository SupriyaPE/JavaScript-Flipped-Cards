from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Product,Category,Banner
from django.contrib.auth.decorators import login_required


def product_list(request):
    query = request.GET.get('q')
    alpha = request.GET.get('alpha')
    min_price = request.GET.get('min')
    max_price = request.GET.get('max')

    products = Product.objects.all()
    categories = Category.objects.all()
    banners = Banner.objects.filter(is_active=True)
    show_banner = True
    no_results = False

    if query or alpha or min_price or max_price:
        show_banner = False

    if query:
        products = products.filter(category__name__icontains=query)
  
    if alpha:
        products = products.filter(title__istartswith=alpha)

    if min_price:
        products = products.filter(price__gte=min_price)

    if max_price:
        products = products.filter(price__lte=max_price)

    if not products.exists():
        no_results = True         

    return render(request, 'products.html',
        {
            'products': products,
            "categories":categories,
            'no_results': no_results,
            'banners':banners,
            'show_banner':show_banner,
            'query': query
        }
    )



def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(request.GET.get("next") or "product")

        return render(request, "login.html", {"error": "Invalid credentials"})

    return render(request, "login.html")

def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {"error": "Username already exists"})

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        return redirect("login")
    return render(request, "register.html")


def logout_view(request):
    logout(request)
    return redirect("product")    



@login_required
def profile_view(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})