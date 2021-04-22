from django.urls import path

from .views import ProductListView,FilterView

urlpatterns = [
    path('', ProductListView.as_view()),
    path('/filter', FilterView.as_view()),
]