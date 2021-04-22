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

        products = Product.objects.filter(q)

        if pick:
            products = products.filter(sub_category__category__name=pick)[:4]

        if discount:
            products = products.order_by('-discount_rate')[:6]

        if new:
            products = products.order_by('-created_at')[:4]

        result = [{
                    'id'             : product.id,
                    'created_at'     : product.created_at,
                    'name'           : product.name,
                    'image_url'      : [product_image.image_url for product_image in product.productimage_set.all()],
                    'original_price' : product.get_real_price()['original_price'],
                    'real_price'     : format(int(product.get_real_price()['real_price']), ','),
                    'discount_rate'  : int(product.discount_rate),
        } for product in products]

        return JsonResponse({'result': result}, status=200)

class FilterView(View):
    def get(self, request):
        category = request.GET.get('category')
        sub_category = request.GET.get('sub_category')
        filter = request.GET.get('filter')

        q = Q()

        if category:
            q &= Q(sub_category__category__name=category)

        if sub_category:
            q &= Q(sub_category__name=sub_category)

        products = Product.objects.filter(q)

        if filter:
            if filter == '최신순':
                products = Product.objects.order_by('-created_at')
            if filter == '낮은가격순':
                products = sorted(products, key=lambda x: x.original_price)
            if filter == '높은가격순':
                products = sorted(products, key=lambda x: x.original_price, reverse=True)

        result = [{
                    'id': product.id,
                    'created_at': product.created_at,
                    'name': product.name,
                    'image_url': [product_image.image_url for product_image in product.productimage_set.all()],
                    'original_price': product.get_real_price()['original_price'],
                    'real_price': format(int(product.get_real_price()['real_price']), ','),
                    'discount_rate': int(product.discount_rate),
        } for product in products]

        return JsonResponse({'result': result}, status= 200)