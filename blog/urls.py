from django.urls import path

from .views import PostDetailsView, PostListView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path("posts/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
    path("posts/<int:pk>/update/", PostUpdateView.as_view(), name="post_update"),
    path("posts/create/", PostCreateView.as_view(), name="post_create"),
    path("post/<int:pk>/", PostDetailsView.as_view(), name="post_details"),
    path("", PostListView.as_view(), name="home")
]