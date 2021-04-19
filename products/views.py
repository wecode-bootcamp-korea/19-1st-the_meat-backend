import json

from django.http.response import JsonResponse
from django.views         import View

from .models import Category,SubCategory,Product,ProductImage

class CategoryView(View):
    def get(self, request):
        result = []
        categories = Category.objects.all()
        for category in categories:
            result.append(
                {
                    'id'   : category.id,
                    'name' : category.name,
                }
            )
        return JsonResponse({'MESSAGE': result}, status=201)

class SubCategoryView(View):
    def get(self, request):
        result = []
        subcategories = SubCategory.objects.exclude(name='전체')
        for subcategory in subcategories:
            result.append(
                {
                    'id'   : subcategory.id,
                    'name' : subcategory.name,
                }
            )
        return JsonResponse({'MESSAGE': result}, status=201)

class SaleproductView(View):
    def get(self, request):
        products = Product.objects.order_by('-discount_rate')[:6]
        result = []
        for product in products:
            productimages = product.productimage_set.all()
            for productimage in productimages:
                result.append(
                    {
                        'id'           : product.id,
                        'name'         : product.name,
                        'image_url'    : productimage.image_url,
                        'price'        : product.get_real_price()['real_price'],
                        'real_price'   : product.original_price,
                        'discount_rate': product.discount_rate,
                    }
                )
        return JsonResponse({'MESSAGE': result}, status=201)

class MdpickView(View):
    def get(self, request, category_id):
        products = Product.objects.filter(sub_category__category__id=category_id)[:4]
        result = []
        for product in products:
            productimages = product.productimage_set.all()
            result.append(
                {
                    'id'           : product.id,
                    'name'         : product.name,
                    'image_url'    : [productimage.image_url for productimage in productimages],
                    'price'        : product.get_real_price()['real_price'],
                    'real_price'   : product.original_price,
                    'discount_rate': product.discount_rate,
                }
            )
        return JsonResponse({'MESSAGE': result}, status=201)

class CategorypageView(View):
    def get(self, request, subcategory_id):

        if not subcategory_id in {obj.id for obj in SubCategory.objects.filter(name='전체')}:
            product_lists = []
            products = Product.objects.filter(sub_category__id = subcategory_id)
            product_lists += list(products)

        else:
            product_lists = []
            category_ids = SubCategory.objects.get(id=subcategory_id)
            if subcategory_id == category_ids.category_id:
                product_lists = Product.objects.filter(sub_category__category__id=category_ids.category_id)

        product_list = []
        for product in product_lists:
            productimages = ProductImage.objects.filter(product=product)
            product_list.append(
                {
                    'id'             : product.id,
                    'name'           : product.name,
                    'price'          : product.get_real_price()['real_price'],
                    'real_price'     : product.original_price,
                    'discount_rate'  : product.discount_rate,
                    'image_url'      : [product.image_url for product in productimages],
                }
            )
        return JsonResponse({'MESSAGE': product_list}, status=201)