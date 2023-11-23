from django.contrib import admin
from .models import Player, Coach, LeaderBoard, Match
# Register your models here.

admin.site.register(Player)
admin.site.register(Coach)
admin.site.register(LeaderBoard)
admin.site.register(Match)