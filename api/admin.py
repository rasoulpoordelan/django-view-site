from django.contrib import admin
from .models import TrainInfo,Prop,Image


class ImageInline(admin.TabularInline):
    model = Image


class TrainAdmin(admin.ModelAdmin):
    inlines = [ImageInline]   
    list_display = ('train_num','name',)

admin.site.register(TrainInfo, TrainAdmin)
    

@admin.register(Prop)
class PropAdmin(admin.ModelAdmin):
    list_display = ('name',)
    