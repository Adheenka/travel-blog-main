from audioop import reverse
from datetime import datetime
from urllib import request
from .forms import CommentForm
import comments as comments
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponseRedirect, JsonResponse
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post,Like
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from hitcount.views import HitCountDetailView

# def home(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, 'blog/home.html', context)


def about(request):

    render(request, 'blog/home.html')


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ["-date_posted"]
    form = CommentForm


class PostDetailView(LoginRequiredMixin,HitCountDetailView):
    model = Post
    count_hit = True




class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','picture', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # def test_func(self):
    #     post = self.get_object()
    #     if self.request.user == post.author:
    #         return True
    #     return False


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','picture','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
def comment(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST, request.FILES)
        if comment_form.is_valid():
            comment_form.instance.user = request.user
            comment_form.instance.post = post

            comment_form.save()

            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def like(request, post_id):
    user = request.user
    post = Post.objects.get(pk=post_id)
    like = Like.objects.filter(user=user, post=post)
    if like:
        like.delete()
    else:
        new_like = Like(user=user, post=post)
        new_like.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))