from django.shortcuts import render

#importando a classe Post
from .models import Post

#importando timezone
from django.utils import timezone

#importando o objeto para mensagem 'page not found'

from django.shortcuts import render, get_object_or_404

# Create your views here.

def post_list(request):
    
    #querySet para publicar no site as postagens em ordem de criação:
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})