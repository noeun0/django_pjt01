from django.shortcuts import render,redirect
from .models import Page

# Create your views here.
def index(request): # 게시글 읽기

    pages = Page.objects.all()
    context = {'pages': pages}
    return render(request, 'pages/index.html',context)

def detail(request,pk): # 게시글 세부 페이지
    page = Page.objects.get(pk=pk)
    context = {'page' : page}
    return render(request, 'pages/detail.html', context)




def upload(request,pk): # 게시글 수정
    pass

def delete(request,pk): # 게시글 삭제
    pass