from django.contrib import admin

# Register your models here.
from .models import Room, Tag, Message

admin.site.register(Room)
admin.site.register(Tag)
admin.site.register(Message)