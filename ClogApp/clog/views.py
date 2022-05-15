from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.
def post_list(request):
    all_post = Post.objects.all()
    return render(request,'clog/index.html',{'post':all_post})
    return HttpResponse(all_post)
