from multiprocessing import Value
from re import template
from django.shortcuts import get_object_or_404, render
from .models import *
# Create your views here.
def show_all(request):
    
    war = War.objects.all()
    data = {'war': war}
    return render(request, 'main/index.html', data)


def main_page(request):
    return render(request, 'main/mian.html')

def news(request):
    news = News.objects.all()
    data={'news': news}
    return render(request, 'main/news.html', data)

def signup(request):
    return render(request, 'main/signup.html')

def moreinfo(request, War_slug):
    war_info = get_object_or_404(War, slug=War_slug)

    data ={
        'War_id': War_slug,
        'warinfo' : war_info
    }
    return render(request, 'main/moreinfo.html', data)

def SearchView(request): # search view
    if request.method == 'POST':
        searched = request.POST['searched']
        war = War.objects.filter(name__contains=searched)
        context={
            'searched': searched,
            'war': war,
                 }
        return render(request, "main/search.html", context )# render
    else:
        context={}
        return render(request, "main/search.html", context )# render
    
def extroInfo(requst):
    f_id = Player.objects.all()
    all = Player_roll.objects.filter(name='Основной состав')
    data={'f_id': f_id}
    return render(requst, 'main/extroInfo.html', data)\
        
def newsinfo(requst, news_slug):
    
    news_info = get_object_or_404(News, slug=news_slug)

    data ={
        'news_slug': news_slug,
        'news_info' : news_info
    }
    return render(requst, 'main/moreinfonews.html', data)

def searchNews(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        news = News.objects.filter(title__contains=searched)
        context={
            'searched': searched,
            'news': news,
                 }
        return render(request, "main/newssearch.html", context )# render
    else:
        context={}
        return render(request, "main/newssearch.html", context )# render
    
def events(request):
    event = Event.objects.all()
    data = {
        'event' : event
    }   
    return render(request, 'main/events.html', data)
def eventinfo(request, event_slug):
    evente = get_object_or_404(Event, slug=event_slug)
    data = {
        'event_slug': event_slug,
        'evente' : evente
    }
    return render(request, 'main/eventinfo.html', data)