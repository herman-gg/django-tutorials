from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post


class PostListView(ListView):
    model = Post
    template_name = "posts/list.html"
    context_object_name = "posts"


class PostDetailsView(DetailView):
    model = Post
    template_name = "posts/details.html"


class PostCreateView(CreateView):
    model = Post
    template_name = "posts/create.html"
    fields = ["title", "author", "body"]


class PostUpdateView(UpdateView):
    model = Post
    template_name = "posts/update.html"
    fields = ["title", "body"]


class PostDeleteView(DeleteView):
    model = Post
    template_name = "posts/delete.html"
    success_url = reverse_lazy("home")

# def posts_list(request):
#     posts = Post.objects.all()
#     return render(request, "posts/list.html", { "posts": posts })


# def post_details(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, "posts/details.html", { "post": post })