from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from .views import BookingViewSet
from rest_framework.authtoken.views import obtain_auth_token
router = DefaultRouter()
router.register(r'tables',BookingViewSet)
urlpatterns = [
    path('',views.index,name='index'),
    path('booking/',include(router.urls)),
    path('api/',obtain_auth_token),
    path('home',views.home,name='home'),
    path('menu',views.MenuItemView.as_view(),name='menu-list-create'),
    path('menu/<int:pk>',views.SingleMenuItemView.as_view(),name='menu-update-delete')
]