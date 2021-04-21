from django.http      import JsonResponse
from django.views     import View

from products.models  import Product
from orders.models    import ProductOrder
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

        # if pick:
        #     q &= Q(sub_category__category__name=pick)[:4]

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