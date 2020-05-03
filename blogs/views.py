from django.shortcuts import render
from .models import Blog

# Create your views here.
def index(request):
    blogs = Blog.objects.order_by('-created_datetime')
    return render(request, 'blogs/index.html', {'blogs': blogs})
    # ユーザーからのrequest情報をもとに、index.htmlを返す
    # {}の中はテンプレート(HTML)に渡したいデータを自由に定義することができる。
    #上の一行で定義したクエリセットを'blogs'キーに渡している

def detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    return render(request, 'blogs/detail.html', {'blog': blog})