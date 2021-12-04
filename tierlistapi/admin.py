from django.contrib import admin
from .models import Character, Profile, Tierlist, Game
# Register your models here.
admin.site.register(Tierlist)
admin.site.register(Game)
admin.site.register(Character)
admin.site.register(Profile)