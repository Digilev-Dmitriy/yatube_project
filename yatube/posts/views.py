from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')


def group_posts(request, slug):
    return HttpResponse(f'Сообщения от {slug}.')


def posts(request):
    return HttpResponse('Все сообщения.')