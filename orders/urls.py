from django.urls import path

from .views import CartView, OrderBuyView

urlpatterns = [
    path('/cart', CartView.as_view()),
    path('/buy', OrderBuyView.as_view()),
]