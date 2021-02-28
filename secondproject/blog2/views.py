from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
# Create your views here.
def home(request):
    blogs= Blog.objects
    return render(request, 'home.html',{'blogs':blogs})

def detail(request, blog_id):
    blog_detail= get_object_or_404(Blog ,pk=blog_id) 
    return render(request, 'detail.html',{'blog':blog_detail})

def new(request):
    return render(request, 'new.html')

def create(request):#입력받은 내용을 DB에 넣어주는 함수
    blog=Blog()
    blog.title= request.GET['title']
    blog.body=request.GET['body']
    blog.pub_date=timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))
    #url은 문자형이기 떄문에 str로 형변환 필요 