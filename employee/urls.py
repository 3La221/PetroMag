from django.urls import path,include
from .views import home ,ajout_obv,download_excel,login_view,logout_view

urlpatterns = [
    path('login/',login_view,name="login"),
    path('logout/',logout_view,name="logout"),
    
    path('',home,name="home"),
    
    path('add/<int:matricule>/',ajout_obv,name="add"),
    
    path('download/<int:matricule>/',download_excel,name="download_excel"),
    
]
