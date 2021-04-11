from django.urls import path, include
from .views import magazine_view, index, contact_view, story_detail_view, story_create_view, story_list_view, your_story_list_view
from users_app import views as users_view

urlpatterns = [
    path('', index, name="index"),
    path('magazine/', magazine_view, name="magazine"),
    path('details/', story_detail_view, name="stories"),
    path('your_stories/', your_story_list_view, name="your_stories"),
    path('stories/', story_list_view, name="list"),
    path('create/', story_create_view, name="create"),
    path('contact/', contact_view, name="contact"),
]
