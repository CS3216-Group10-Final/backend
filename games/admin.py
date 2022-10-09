from django.contrib import admin

from .models import Game, GameEntry, Genre, Platform

admin.site.register(Game)
admin.site.register(GameEntry)
admin.site.register(Genre)
admin.site.register(Platform)
