from django.contrib import admin
from django.urls import path
from gaming import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('game/', views.game_view, name='game'),
]