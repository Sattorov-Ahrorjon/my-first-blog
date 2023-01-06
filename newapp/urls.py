from django.urls import path
from .views import HomePageView, get_admin_url

urlpatterns = [
    path('', HomePageView.as_view(), name='name_home'),
    path('admin/', get_admin_url, name='name_admin'),
]
