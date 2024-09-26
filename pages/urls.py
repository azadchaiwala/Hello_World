from django.urls import path

from pages.views import HomeView,aboutView,contactView,cartView

urlpatterns = [
    path('',HomeView.as_view(), name = 'index'),
    path('about/',aboutView, name = 'about'),
    path('contact/',contactView.as_view(), name = 'contact'),
    path('cart/',cartView.as_view(), name = 'cart'),
]