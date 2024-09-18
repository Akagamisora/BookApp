from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static

def home(request):
    return render(request, 'home.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', home, name='home'),
]

if settings.DEBUG:  # 開発環境のみ静的ファイルを提供する設定
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])