from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # 管理画面
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),
]
