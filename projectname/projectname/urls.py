
from django.contrib import admin
from django.urls import path
import appname.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',appname.views.index,name='index'),
    path('board/',appname.views.board,name="board"),
    path('write/',appname.views.write,name='write'),
    path('writeSend/',appname.views.writeSend,name='writeSend'),
    path('detail/<int:writeNumber>',appname.views.detail,name="detail"),
]
