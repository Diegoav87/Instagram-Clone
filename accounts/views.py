from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, user_permission
from .forms import UserCreateForm, ProfileForm
from .models import Profile, Follower
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.

@unauthenticated_user
def signup(request):
    form = UserCreateForm()

    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(user=user)
            return redirect('accounts:login')

    return render(request, 'accounts/signup.html', {'form': form})

@unauthenticated_user
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('posts:post_list')
        else:
            messages.info(request, 'Username or password is incorrect')

    return render(request, 'accounts/login.html', {})

@login_required
def logout_user(request):
    logout(request)
    return redirect('accounts:login')

@login_required
def user_profile(request, username):
    user = User.objects.get(username__iexact=username)
    followed = False
    for follower in user.followers.all():
        if request.user == follower.user:
            followed = True
            break

    return render(request, 'accounts/user_profile.html', {'target_user': user, 'followed': followed})

@login_required
@user_permission
def edit_profile(request, username):
    user = User.objects.get(username__iexact=username)
    form = ProfileForm(instance=user.profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user.profile)

        if form.is_valid():
            form.save()
            return redirect('accounts:user_profile', username=username)

    return render(request, 'accounts/edit_profile.html', {'form': form})

@login_required
def follow(request, username):
    user = User.objects.get(username__iexact=username)
    follower = Follower.objects.create(user=request.user, followed_user=user)

    return redirect('accounts:user_profile', username=username)

@login_required
def unfollow(request, username):
    user = User.objects.get(username__iexact=username)

    for follower in user.followers.all():
        if request.user == follower.user:
            follower.delete()
            break

    return redirect('accounts:user_profile', username=username)


