from django.urls import path
from . import views

# URLConf Module (URL Configurations) Rememner to import into main config ventureinsight_prj/urls.py
urlpatterns = [
    path('signup/', views.signup),
    path('login/', views.login),
    path('dashboard/', views.dashboard),
    path('companyinfo/', views.companyinfo),
    path('profile/', views.profile),
    path('', views.home),
    path('logout/', views.logout)
    
]