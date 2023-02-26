from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(request):
    template = 'posts/index.html'
    posts = Post.objects.order_by('-pub_date')[:10]
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
        'title': 'Последние записи на сайте'
    }
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'posts': posts,
        'group': group,
        'title': f'Записи сообщества {group}'
    }
    return render(request, 'posts/group_list.html', context)


def posts(request):
    return HttpResponse('Все сообщения.')
