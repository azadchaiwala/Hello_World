from django.urls import path

from pages.views import homeview,aboutView,contactView,cartView

urlpatterns = [
    path('home/',homeview.as_view()),
    path('about/',aboutView),
    path('contact/',contactView),
    path('cart/',cartView),
]