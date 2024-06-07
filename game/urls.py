from django.contrib import admin
from django.urls import path
from gaming import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('main/', views.main, name='main'),
    path('game/', views.game_view, name='game'),
    path('fight/', views.fight_monster, name='fight_monster'),
    path('battle/<int:monster_id>/', views.battle, name='battle'),
]