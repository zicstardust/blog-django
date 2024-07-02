from django.shortcuts import render
from .models import Posts

# Create your views here.

def post_list(request):
    template_name = 'post-list.html'
    posts = Posts.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, template_name, context)