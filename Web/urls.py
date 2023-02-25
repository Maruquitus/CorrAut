from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.redirect, name="redirecionar"),
    path('login/', views.login, name='login'),
    path('checar/', views.checar, name='checar'),
    path('turmas/', views.turmasPag, name="turmas"),
    path('cadastro/', views.cadgab, name="cadastroGab"),
    path('dashboard/', views.dashboard, name="dashboard"),
    #path('setCookie/', views.setCookie, name="setCookie")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
