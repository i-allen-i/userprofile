
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_view),
    path('listview/',views.listuser),
    path('detailsview/<int:user_id>/', views.detailsview,name="details"),
    path('updateview/<int:user_id>/', views.updateuser,name="update"),
]
