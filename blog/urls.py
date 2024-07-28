from django.urls import path

from .views import posts_list, post_details

urlpatterns = [
    path("post/<int:pk>/", post_details, name="post_details"),
    path("", posts_list, name="home")
]