from django.urls import path

<<<<<<< HEAD
from .views import AddCartView

urlpatterns = [
    path('/addcart', AddCartView.as_view()),
=======
from .views import OrderView

urlpatterns = [
    path('orders', OrderView.as_view()),
>>>>>>> e4a0d7aecc0ce68ec3c0f9943a0a1c013cfff408
]