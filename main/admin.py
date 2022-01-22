from django.contrib import admin
from .models import *
# Register your models here.
class warAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}
class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}
class eventAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}
admin.site.register(Map)
admin.site.register(Player)
admin.site.register(Player_roll)
admin.site.register(War, warAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Event, eventAdmin)