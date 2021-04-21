from django.http      import JsonResponse
from django.views     import View

from products.models  import Product
from django.db.models import Q

class ProductListView(View):
    def get(self, request):
        category     = request.GET.get('category', None)
        sub_category = request.GET.get('sub_category', None)
        pick         = request.GET.get('pick', None)
        discount     = request.GET.get('discount', None)
        new          = request.GET.get('new', None)

        q = Q()

        if category:
            q &= Q(sub_category__category__name=category)

        if sub_category:
            q &= Q(sub_category__name=sub_category)

        if pick:
            q &= Q(sub_category__category__name=pick)

        products = Product.objects.filter(q)

        if discount:
            products = products.order_by('-discount_rate')[:6]

        if new:
            products = products.order_by('-created_at')[:4]

        result = [{
                    'id'           : product.id,
                    'created_at'   : product.created_at,
                    'name'         : product.name,
                    'image_url'    : [product_image.image_url for product_image in product.productimage_set.all()],
                    'price'        : int(product.get_real_price()['real_price']),
                    'real_price'   : int(product.original_price),
                    'discount_rate': int(product.discount_rate),
        } for product in products]

        return JsonResponse({'result': result}, status=200)

#인기순, 최신순, 가격순(낮은, 높은)
class SortView(View):
    def get(self, request):
        category = request.GET.get('category')
        sub_category = request.GET.get('sub_category')
        popular = request.GET.get('popular')
        new = request.GET.get('new')
        high_price = request.GET.get('high_price')
        low_price = request.GET.get('low_price')



        if category:
            products = Product.objects.filter(sub_category__category__name=category)

        if sub_category:
            products = Product.objects.filter(sub_category__name=sub_category)

        if popular:
            products = Product.objects.all()
            for product in products:
                order = product.productorder_set.filter(order__status__status_name='배송완료')
                quantities = order.order_by('-quantity')

        if new:
            products = Product.objects.order_by('-created_at')

        if high_price:
            products = Product.objects.all()
            high_price = sorted(products, key=lambda x: x.original_price)

        if low_price:
            products = Product.objects.all()
            low_price = sorted(products, key=lambda x: -x.original_price)

