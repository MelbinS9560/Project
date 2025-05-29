from django.urls import path
from . import views

urlpatterns = [
    path('submit-feedback/', views.submit_feedback, name='submit_feedback'),
    path('feedback/', views.feedback_page, name='feedback_page'),  # ✅ Add this
]
