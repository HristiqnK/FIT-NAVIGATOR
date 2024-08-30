from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from FitNavigator import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .tokens import generate_token

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Потребителското име вече съществува!")
        elif len(username) > 10:
            messages.error(request, "Потребителското име трябва да е под 15 знака!")
        elif not username.isalnum():
            messages.error(request, "Потребителското име може да съдържа само букви и числа!")
        else:
            myuser = User.objects.create_user(username, email, password)
            myuser.save()
            myuser.is_active = True
            return redirect('signup')
            
    return render(request, "authentication/signup.html")

# def activate(request,uidb64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active = True
        # user.profile.signup_confirmation = True
        myuser.save()
        login(request,myuser)
        messages.success(request, "Профилат ви беше активиран!")
        return redirect('signin')
    else:
        return render(request,'activation_failed.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('account')  # redirect to account view instead of rendering the template directly

        else:
            messages.error(request, "Invalid username or password.")
            return render(request, "authentication/signin.html")
        
    return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!")
    return redirect('home')

@login_required  # Ensure the user is logged in to access this view
def account(request):
    user = request.user
    return render(request, "authentication/account_page.html", {'username': user.username, 'email': user.email})