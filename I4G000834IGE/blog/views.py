from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse
# from django.views.generic import (CreateView, DeleteView, UpdateView)
# from django.views.generic import (ListView, DetailView)
from .models import Post
# Create your views here.
#from django import Post
from django.views import generic


class PostListView(generic.ListView):
    model = Post

class PostCreateView(generic.CreateView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")

class PostDetailView(generic.DetailView):
    model = Post

class PostUpdateView(generic.UpdateView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")

class PostDeleteView(generic.DeleteView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")