from django.urls import path 
from . import views
app_name = 'todo_app'

urlpatterns = [
    path('',views.HomePage.as_view(),name='index'),
    path('<int:pk>/',views.PostDetailView.as_view(),name = 'detail'),
    path('new/',views.CreateNewPost.as_view(),name='create'),
    path('delete/<int:pk>',views.deleteItem.as_view(),name='delete'),
    path('update/<int:pk>',views.updateItem.as_view(),name='update')
]
