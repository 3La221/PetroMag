from django.urls import path,include
from .views import home ,ajout_obv,download_excel


urlpatterns = [
    path('',home,name="home"),
    path('add/<int:matricule>/',ajout_obv,name="add"),
    path('download/?<int:matricule>/',download_excel,name="download_excel")
]
