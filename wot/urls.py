"""wot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from main.views import *
from main.models import War
urlpatterns = [
    path('admin/', admin.site.urls),
    path('extra-info/', extroInfo),
    path('wars/search/', SearchView, name='SearchForSmt'),
    path('', main_page),
    path('wars/', show_all),
    path('events', events),
    path('events/<slug:event_slug>/', eventinfo),
    path('wars/<slug:War_slug>/', moreinfo),
    path('news/', news),
    path('news/search/',searchNews, name='searchForNews'),
    path('news/more/<slug:news_slug>/', newsinfo),
    path('signup/', signup),



]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)