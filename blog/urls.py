from . import views
from django.urls import path

urlpatterns = [
    path('a', views.allblogs, name='allblogs'),
    path('<int:b_id>', views.detail, name='detail'),
]
