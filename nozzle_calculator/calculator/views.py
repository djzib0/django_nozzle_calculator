from django.shortcuts import render, redirect
from .models import Nozzle, Order
from .forms import NozzleForm, OrderForm
from .filters import NozzleFilter

from .functions import translate_type_name

# Create your views here.
def index_view(request):
    context = {}
    template = 'calculator/index.html'

    return render(request, template, context)


def nozzles_view(request):
    nozzles = Nozzle.objects.all()
    nozzle_filter = NozzleFilter(request.GET,
                                 queryset=nozzles)
    nozzles = nozzle_filter.qs

    context = {'nozzles': nozzles,
               'nozzle_filter': nozzle_filter,
               }
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
    existing_orders_count = 0
    if request.method != 'POST':
        form = OrderForm()
    else:
        form = OrderForm(data=request.POST)
        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.nozzle = nozzle
            existing_orders_count = Order.objects.filter(order_dmcg_number=new_order.order_dmcg_number).count()
            if existing_orders_count < 1:
                new_order.save()
                return redirect('calculator:nozzle_orders', nozzle.id)
            else:

                context = {'form': form,
                           'nozzle_id': nozzle.id,
                           'nozzle': nozzle,
                           }
                template = 'calculator/add_nozzle_order.html'

                return render(request, template, context)

    context = {'form': form,
               'nozzle_id': nozzle.id,
               'nozzle': nozzle,
               }
    template = 'calculator/add_nozzle_order.html'

    return render(request, template, context)


def show_order_exist(request, nozzle_id):
    nozzle = Nozzle.objects.get(id=nozzle_id)

    context = {'nozzle': nozzle}
    template = 'calculator/order_exist_message.html'

    return render(request, template, context)
