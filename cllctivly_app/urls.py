from django.urls import path
from .views import HomeView,DiscoverView

app_name = 'cllctivly_app'

urlpatterns = [
    path('',HomeView.as_view(),name="home"),
    path('discover/',DiscoverView.as_view(),name="discover"),
]