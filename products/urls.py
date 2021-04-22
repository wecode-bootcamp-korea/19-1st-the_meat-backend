from django.urls import path, include

<<<<<<< HEAD
from .views import ProductView, ProductDetailView

urlpatterns = [
    path('/detail/<int:id>', ProductDetailView.as_view()),
=======
from .views import ProductListView

urlpatterns = [
    path('', ProductListView.as_view()),
>>>>>>> main
]