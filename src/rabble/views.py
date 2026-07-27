from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.http import HttpResponse
from .models import Communities, Subrabbles, Posts, Comments
from django.urls import reverse
from django.shortcuts import redirect

def index(request):
    default_community = Communities.objects.filter(community_name="default").first()
    subrabbles = Subrabbles.objects.filter(community=default_community)
    return render(request, 'rabble/index.html', {'subrabbles': subrabbles})

def subrabble_detail(request, identifier):
    subrabble = get_object_or_404(Subrabbles, identifier=identifier)
    posts = Posts.objects.filter(subrabble=subrabble)
    return render(request, "rabble/subrabble_detail.html", {
        "subrabble": subrabble,
        "posts": posts,
    })

def post_detail(request, identifier, pk):
    subrabble = get_object_or_404(Subrabbles, identifier=identifier)
    post = get_object_or_404(Posts, pk=pk, subrabble=subrabble)
    comments = Comments.objects.filter(post=post)

    return render(request, 'rabble/post_detail.html', {
        'subrabble': subrabble,
        'post': post,
        'comments': comments
    })

def profile(request):
    return render(request, "rabble/profile.html")

def post_create(request, identifier):
    subrabble = get_object_or_404(Subrabbles, identifier=identifier)

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.subrabble = subrabble
            post.user = request.user
            post.save()
            return redirect(reverse('post-detail', args=[identifier, post.pk]))
    else:
        form = PostForm()
    return render(request, 'rabble/post_form.html', {
        'form': form,
        'subrabble': subrabble
    })

def post_edit(request, identifier, pk):
    subrabble = get_object_or_404(Subrabbles, identifier=identifier)
    post = get_object_or_404(Posts, pk=pk, subrabble=subrabble)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post-detail', identifier=subrabble.subrabble_name, pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'rabble/post_form.html', {
        'form': form,
        'subrabble': subrabble,
        'post': post,
        'is_edit': True,
    })
