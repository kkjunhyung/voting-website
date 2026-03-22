from django.contrib import admin
from .models import VoteItem

class ProjectAdmin(admin.ModelAdmin):
    fields = ('title', 'description', 'votes', 'image')  # ⭐ 핵심

admin.site.register(VoteItem)