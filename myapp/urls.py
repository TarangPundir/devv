from django.urls import path
from . import views

urlpatterns = [
    path('list', views.List, name="list"),
    path('view/<int:id>', views.view, name="view"),
    path('create', views.create, name="create"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('update/<int:id>', views.update, name="update")
]
