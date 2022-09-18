from django.urls import path
from . import views

urlpatterns = [
    path('docinfos', views.list),
    path('docinfos/new', views.DocInfosCreateView.as_view(), name = "docinfos.new")
]