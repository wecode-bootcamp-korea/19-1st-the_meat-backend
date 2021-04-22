from django.urls import path

from .views import AddressView, UserView, LoginView

urlpatterns = [
    path('/users', UserView.as_view()),
    path('/login', LoginView.as_view()),
    path('/address', AddressView.as_view())
]
