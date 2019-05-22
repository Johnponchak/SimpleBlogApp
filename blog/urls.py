from . import views
from django.urls import path

urlpatterns = [
    path('blog/', views.PostList, name='PostList'),
    path('<slug:ur>/', views.PostDetail, name='PostDetail'),
]