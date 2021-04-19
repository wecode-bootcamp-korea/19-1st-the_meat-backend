from django.urls import path

from .views import CategorypageView,SubCategoryView,CategoryView,SaleproductView,MdpickView

urlpatterns = [
    path('/category/<int:subcategory_id>',CategorypageView.as_view()),
    path('/subcategory', SubCategoryView.as_view()),
    path('/category', CategoryView.as_view()),
    path('/sale', SaleproductView.as_view()),
    path('/mdpick/<int:category_id>', MdpickView.as_view())
]