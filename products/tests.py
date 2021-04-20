from django.test import TestCase

# Create your tests here.

from django.http      import JsonResponse
from django.views     import View

from products.models import Product

class ProductListView(View):
    def get(self, request):
        category = request.GET.get('category', None)
        sub_category = request.GET.get('sub_category', None)
        discount = request.GET.get('discount', None)
        new = request.GET.get('new', None)
        pick = request.GET.get('pick', None)

        products = Product.objects.all()
        # /products 만 나올때 어떻게?

        if category:
            products = products.filter(sub_category__category__name=category)

        if sub_category:
            products = products.filter(sub_category__name=sub_category)

        if pick:
            products = products.filter(sub_category__category__name=pick)[:4]

        if discount:
            products = products.order_by('-discount_rate')[:6]

        if new:
            products = products.order_by('-created_at')[:4]

        result = [{
                    'id'           : product.id,
                    'sub_category' : product.sub_category.name,
                    'category'     : product.sub_category.category.name,
                    'created_at'   : product.created_at,
                    'name'         : product.name,
                    'image_url'    : [product_image.image_url for product_image in product.productimage_set.all()],
                    'price'        : int(float(product.get_real_price()['real_price'])),
                    'real_price'   : int(float(product.original_price)),
                    'discount_rate': int(float(product.discount_rate)),
        } for product in products]

        return JsonResponse({'result': result}, status=200)

