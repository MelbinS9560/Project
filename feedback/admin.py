from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'message', 'submitted_at')
    list_filter = ('rating', 'submitted_at')
    search_fields = ('name', 'message')
