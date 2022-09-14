from django.shortcuts import render, redirect
from .models import Nozzle, Order
from .forms import NozzleForm, OrderForm

from .functions import translate_type_name

# Create your views here.
def index_view(request):
    context = {}
    template = 'calculator/index.html'

    return render(request, template, context)


def nozzles_view(request):
    nozzles = Nozzle.objects.all()

    context = {'nozzles': nozzles}
    template = 'calculator/nozzles.html'

    return render(request, template, context)


def nozzle_details_view(request, nozzle_id):
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


def nozzle_orders_view(request, nozzle_id):
    nozzle = Nozzle.objects.get(id=nozzle_id)
    orders = nozzle.order_set.order_by('-date_created')
    ratio = round((nozzle.profile_height / nozzle.diameter), 1)

    context = {'nozzle': nozzle,
               'orders': orders,
               'ratio': ratio,
               }
    template = 'calculator/nozzle-orders.html'

    return render(request, template, context)

def add_nozzle_order(request, nozzle_id):
    nozzle = Nozzle.objects.get(id=nozzle_id)
    if request.method != 'POST':
        form = OrderForm()
    else:
        form = OrderForm(data=request.POST)
        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.nozzle = nozzle
            new_order.save()
            return redirect('calculator:nozzle_orders', nozzle.id)

    context = {'form': form,
               'nozzle_id': nozzle.id,
               'nozzle': nozzle}
    template = 'calculator/add_nozzle_order.html'

    return render(request, template, context)

