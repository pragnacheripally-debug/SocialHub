from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Like
from .forms import RegisterForm


def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'posts': posts})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('/login')

    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form': form})


@login_required
def create_post(request):
    if request.method == 'POST':
        content = request.POST['content']

        Post.objects.create(
            user=request.user,
            content=content
        )

    return redirect('/')


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if post.user == request.user:
        post.delete()

    return redirect('/')


@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    already_liked = Like.objects.filter(
        user=request.user,
        post=post
    )

    if not already_liked:
        Like.objects.create(
            user=request.user,
            post=post
        )

    return redirect('/')