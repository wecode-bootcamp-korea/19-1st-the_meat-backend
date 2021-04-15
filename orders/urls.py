from django.urls import path

from .views import AddCartView

urlpatterns = [
    path('/addcart', AddCartView.as_view()),
]