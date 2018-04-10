from django.shortcuts import render

#importando a classe Post
from .models import Post

#importando timezone
from django.utils import timezone

# Create your views here.

def post_list(request):
    
    #querySet para publicar no site as postagens em ordem de criação:
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

