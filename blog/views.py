from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .models import Cadastro
from .forms import CadForm
from .forms import PostForm
from events.models import Event
from datetime import datetime
from django.utils.timezone import localdate



def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    day = datetime(localdate().year, localdate().month, localdate().day)
    context = {
        'events': Event.objects.filter(
            date='{:%Y-%m-%d}'.format(day)).order_by('-priority', 'event'),
        'form': form
    }
    return render(request, 'blog/post_edit.html', context)

def day():
    day = datetime(localdate().year, localdate().month, localdate().day)
    context = {
        'events': Event.objects.filter(
            date='{:%Y-%m-%d}'.format(day)).order_by('-priority', 'event'),
    }

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    day = datetime(localdate().year, localdate().month, localdate().day)
    context = {
        'events': Event.objects.filter(
            date='{:%Y-%m-%d}'.format(day)).order_by('-priority', 'event'),
        'form': form
    }
    return render(request, 'blog/post_edit.html', context)


def post_cad(request):
    if request.method == "Cadastro":
        form = CadForm(request.Cadastro)
        if form.is_valid():
            Cadastro = form.save(commit=False)
            Cadastro.author = request.user
            Cadastro.published_date = timezone.now()
            Cadastro.save()
            return redirect('cadastro', pk=post.pk)
    else:
        form = CadForm()
    day = datetime(localdate().year, localdate().month, localdate().day)
    context = {
        'events': Event.objects.filter(
            date='{:%Y-%m-%d}'.format(day)).order_by('-priority', 'event'),
        'form': form
    }
    return render(request, 'blog/cadastro.html', context)


def cad_list(request):
    cadastro = Cadastro.objects.all()
    return render(request, 'blog/cadastro_list.html', {'cadastro': cadastro})

def cad_detail(request, pk):
    cadastro = get_object_or_404(Cadastro, pk=pk)
    return render(request, 'blog/cadastro_detail.html', {'cadastro': cadastro})