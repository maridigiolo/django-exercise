from django.contrib import admin

from .models import Poll, Choice, Category

@admin.register(Category)
class CatAdmin(admin.ModelAdmin):
  list_display = ('name', 'slug')

@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
  list_display = ('question', 'slug')
  filter_horizontal = ('categories',)

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
  list_display = ('answer', 'votes', 'question')
