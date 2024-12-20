
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def redirect_to_login(request):
    return redirect('login')

urlpatterns = [
    path('', redirect_to_login),
    path('admin/', admin.site.urls),
    path('AccountManage/', include('AccountManage.urls')),
    path('Board/', include('Board.urls')),
    path('Stock/', include('Stock.urls')),
]
