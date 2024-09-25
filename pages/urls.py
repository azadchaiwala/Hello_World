from django.urls import path

from pages.views import homeView,aboutView,contactView,cartView

urlpatterns = [
    path('home/',homeView.as_view()),
    path('about/',aboutView.as_view()),
    path('contact/',contactView.as_view()),
    path('cart/',cartView.as_view()),
]