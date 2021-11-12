from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Productos
import json

# Create your views here.

class ProductView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    

    def get(self, request, id=0):
        if(id > 0):
            productos = list(Productos.objects.filter(id=id).values())
            if len(productos) > 0:
                product = productos[0]
                datos = {'message': "Success", 'product': product}
            else:
                datos = {'message': "Producto no encontrado..."} 
            return JsonResponse(datos)
        else:
            productos = list(Productos.objects.values())
            if len(productos)>0:
                datos = {'message': "Success", 'productos': productos}
            else:
                datos = {'message': "Productos no encontrados..."}
            return JsonResponse(datos)

    def post(self, request):
        jd = json.loads(request.body)
        Productos.objects.create(name=jd['name'], stock=jd['stock'], price=jd['price'], paused=jd['paused'], images=jd['images'])
        datos = {'message': 'Success'}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        productos = list(Productos.objects.filter(id=id).values())
        if len(productos) > 0:
            productos = Productos.objects.get(id=id)
            productos.name = jd['name']
            productos.stock = jd['stock']
            productos.price = jd['price']
            productos.paused = jd['paused']
            productos.images = jd['images']
            productos.save()
            datos = {'message': 'Success'}
        else:
            datos = {'message': "Producto no encontrado..."} 
        return JsonResponse(datos)
        
    def delete(self, request, id):
        products = list(Productos.objects.filter(id=id).values())
        if len(products) > 0:
            Productos.objects.filter(id=id).delete()
            datos = {'message': 'Success'}
        else:
            datos = {'message': "Producto no encontrado..."}
        return JsonResponse(datos)