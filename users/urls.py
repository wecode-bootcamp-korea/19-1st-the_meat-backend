from django.urls import path

from .views import UserView
from orders.views import CartView

urlpatterns = [
    path('/cart', CartView.as_view()),
]