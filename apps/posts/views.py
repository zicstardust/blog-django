from django.shortcuts import render
from .forms import PostsForm
from .models import Posts
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.

def post_list(request):
    template_name = 'post-list.html'
    posts = Posts.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, template_name, context)


def post_create(request):
    if request.method == 'POST':
        form = PostsForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()

            messages.success(request, 'Post create sucess')
            return HttpResponseRedirect(reverse('post-list'))

    form = PostsForm()
    return render (request, 'post-create.html', {"form": form})
