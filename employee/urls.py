from django.urls import path,include
from .views import home ,ajout_obv


urlpatterns = [
    path('',home,name="home"),
    path('add/<int:matricule>/',ajout_obv,name="add")
]
