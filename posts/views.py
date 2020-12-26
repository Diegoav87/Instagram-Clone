from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.models import User
from accounts.decorators import action_permission

# Create your views here.
@login_required
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/post_list.html', {'posts': posts})

@login_required
def post_detail(request, pk):
    post = Post.objects.get(id=pk)

    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('posts:post_detail', pk=post.pk)


    return render(request, 'posts/post_detail.html', {'post': post, 'form': form})

@login_required
def create_post(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:post_list')

    return render(request, 'posts/create_post.html', {'form': form})

@login_required
@action_permission
def update_post(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()
            return redirect('posts:post_list')
    
    return render(request, 'posts/create_post.html', {'form': form})

@login_required
@action_permission
def delete_post(request, pk):
    post = Post.objects.get(id=pk)

    if request.method =='POST':
        post.delete()
        return redirect('posts:post_list')

    return render(request, 'posts/delete_post.html', {'post': post})

@login_required
def like_post(request, pk):
    post = Post.objects.get(id=pk)
    post.likes += 1
    post.save()
    return redirect('posts:post_list')





