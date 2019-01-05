from django.contrib import admin

# Register your models here.
from .models import newsItem

@admin.register(newsItem)
class newsAdmin(admin.ModelAdmin):
    list_display=['pk','title','publicTime','publicContent','visitCount']