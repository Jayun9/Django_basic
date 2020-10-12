from django.urls import path
from . import views
urlpatterns = [
    path('details/<int:pk>/', views.board_details),
    path('list/',views.board_list),
    path('write/', views.board_write)
]