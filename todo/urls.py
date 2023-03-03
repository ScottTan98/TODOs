from django.urls import path
from . import views
from rest_framework.authtoken import views as view

urlpatterns = [
    path('todos/', views.TodoList, name="TodoList"),
    path('todos/<int:pk>/', views.TodoDetails, name="TodoDetails"),
    path('api-token-auth/', view.obtain_auth_token),

]