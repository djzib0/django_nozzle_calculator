from django.shortcuts import render
from .models import Nozzle, Order

from .functions import translate_type_name

# Create your views here.
def indexView(request):
    context = {}
    template = 'calculator/index.html'

    return render(request, template, context)


def nozzlesView(request):
    nozzles = Nozzle.objects.all()

    context = {'nozzles': nozzles}
    template = 'calculator/nozzles.html'

    return render(request, template, context)


def nozzleDetailsView(request, nozzle_id):
    nozzle = Nozzle.objects.get(id=nozzle_id)
    ratio = round((nozzle.profile_height / nozzle.diameter), 1)
    type_name = translate_type_name(str(nozzle.inner_ring_type))
    orders = Order.objects.all()
    nozzle_total_orders = orders.filter(nozzle=nozzle).count()

    context = {'nozzle': nozzle,
               'ratio': ratio,
               'type_name': type_name,
               'nozzle_total_orders': nozzle_total_orders,
               }
    template = 'calculator/nozzle-details.html'

    return render(request, template, context)


def nozzleOrdersView(request, nozzle_id):
    nozzle = Nozzle.objects.get(id=nozzle_id)
    orders = nozzle.order_set.order_by('-date_created')

    context = {'nozzle': nozzle,
               'orders': orders,
               }
    template = 'calculator/nozzle-orders.html'

    return render(request, template, context)
