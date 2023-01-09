from django.shortcuts import render
from blog.models import Post
from django.db.models import Q

# Create your views here.
def searchResult(request):
    post=None
    query=None
    if 'q' in request.GET:
        query = request.GET.get('q')
        post=Post.objects.all().filter(Q(title__contains=query) | Q(content__contains=query))
        return render(request,'blog/search.html',{'query':query,'post':post})