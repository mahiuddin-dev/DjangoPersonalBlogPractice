from django.urls import path
from . import views


app_name = 'home'
                                              
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('blog/<slug>/', views.BlogView.as_view(), name='blog_details'),
    path('search/', views.SearchView.as_view(), name='search_blog'),
]