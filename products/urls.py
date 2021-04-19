from django.urls import path, include

from .views import ProductView, ProductDetailView

urlpatterns = [
    path('/detail/<int:id>', ProductDetailView.as_view()),
]