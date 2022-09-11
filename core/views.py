from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Profile


def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':  # checking data, if it's incorrect - return to signup page
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():  # checking if user email already taken
                messages.info(request, 'Email Taken.')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():  # checking if username already taken
                messages.info(request, 'Username Taken.')
                return redirect('signup')
            else:  # if userinfo is valid, create user
                user = User.objects.create_user(username=username, email=email, password=password,)
                user.save()

                # Log user in and redirect to settings page

                # create a Profile object for the new user
                user_model = User.objects.get(username=user)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('signup')
        else:
            messages.info(request, 'Password Not Matching.')
            return redirect('signup')

    else:
        return render(request, 'signup.html')
