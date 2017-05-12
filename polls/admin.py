from django.contrib import admin

from .models import Poll, Choice

@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
  list_display = ('question', 'slug')
@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
  list_display = ('answer', 'votes', 'question')
