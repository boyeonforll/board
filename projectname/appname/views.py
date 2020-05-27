from django.shortcuts import render, redirect, get_object_or_404
from .models import Post


# Create your views here.
def index(request):
    return render (request,'index.html')

def board(request):
    newBoard = Post.objects
    return render(request,'board.html',{"boardList":newBoard})

def write(request):
    return render(request,'write.html')

def writeSend(request): 
    boardItem = Post()
    boardItem.title = request.GET['boardTitle']
    boardItem.body = request.GET['boardBody']
    boardItem.save()
    return redirect('board')

def detail(request,writeNumber):
    detailId = get_object_or_404(Post,pk=writeNumber)

    return render(request,'detail.html',{"detailPageId":detailId})

