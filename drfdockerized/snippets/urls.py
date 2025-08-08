from django.urls import include, path
from snippets import views

urlpatterns = [
    path('', views.snippets_list),
    path('<int:pk>/', views.snippet_detail),
]