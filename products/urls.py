from django.urls import path, include

from .views import ProductListView, FilterView, ProductDetailView

urlpatterns = [
    path('', ProductListView.as_view()),
    path('/filter', FilterView.as_view()),
    path('/detail/<int:id>', ProductDetailView.as_view()),
]