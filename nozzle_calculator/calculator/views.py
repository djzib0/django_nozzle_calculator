from django.shortcuts import render, redirect
from django.db.models import Count, Sum
from .models import Nozzle, Order, Offer
from .forms import NozzleForm, OrderForm, OfferForm
from .filters import NozzleFilter, OrderFilter

from .functions import translate_type_name

# Create your views here.
def index_view(request):
    context = {}
    template = 'calculator/index.html'

    return render(request, template, context)


def nozzles_view(request):
    nozzles = Nozzle.objects.all().annotate(order_count=Count('order'))
    nozzle_filter = NozzleFilter(request.GET,
                                 queryset=nozzles)
    nozzles = nozzle_filter.qs

    context = {'nozzles': nozzles,
               'nozzle_filter': nozzle_filter,
               # 'nozzle_orders_count': nozzle_orders_count,
               }
    template = 'calculator/nozzles.html'

    return render(request, template, context)


def nozzle_details_view(request, nozzle_id):
    nozzle = Nozzle.objects.get(id=nozzle_id)
    ratio = round((nozzle.profile_height / nozzle.diameter), 1)
    type_name = translate_type_name(str(nozzle.inner_ring_type))
    orders = Order.objects.all()
    offers = Offer.objects.all()
    nozzle_total_orders = orders.filter(nozzle=nozzle).count()
    nozzle_total_offers = offers.filter(nozzle=nozzle).count()

    context = {'nozzle': nozzle,
               'ratio': ratio,
               'type_name': type_name,
               'nozzle_total_orders': nozzle_total_orders,
               'nozzle_total_offers': nozzle_total_offers,
               'nozzle_id': nozzle_id,
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


def nozzle_offers_view(request, nozzle_id):
    nozzle = Nozzle.objects.get(id=nozzle_id)
    offers = nozzle.offer_set.order_by('dmcg_offer_number')

    context = {'nozzle': nozzle,
               'offers': offers}
    template = 'calculator/nozzle-offers.html'

    return render(request, template, context)


def add_nozzle(request):
    if request.method != 'POST':
        form = NozzleForm()
    else:
        form = NozzleForm(request.POST)
        if form.is_valid():
            new_nozzle = form.save()
            print(new_nozzle.id)
            return redirect('calculator:nozzle_details', new_nozzle.id)

    context = {'form': form}
    template = 'calculator/add_nozzle.html'

    return render(request, template, context)


def edit_nozzle(request, nozzle_id):
    nozzle = Nozzle.objects.get(id=nozzle_id)
    if request.method != 'POST':
        form = NozzleForm(instance=nozzle)
    else:
        form = NozzleForm(instance=nozzle, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('calculator:nozzle_details', nozzle.id)

    context = {'form': form,
               'nozzle': nozzle}
    template = 'calculator/edit_nozzle.html'

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
                message = 'Takie zlecenie już istnieje!'
                context = {'form': form,
                           'message': message,
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


def edit_nozzle_order(request, nozzle_id, order_id):
    nozzle = Nozzle.objects.get(id=nozzle_id)
    order = Order.objects.get(id=order_id)
    # variable for further order exists check
    existing_order = order.order_dmcg_number
    if request.method != 'POST':
        form = OrderForm(instance=order)
    else:
        form = OrderForm(instance=order, data=request.POST)
        if form.is_valid():
            new_order = form.save(commit=False)
            # existing order is the same (no change from user) - do nothing and redirect
            if new_order.order_dmcg_number == existing_order:
                return redirect('calculator:nozzle_orders', nozzle.id)
            # if the order is different, first check whether it already exists
            else:
                existing_orders_count = Order.objects.filter(order_dmcg_number=new_order.order_dmcg_number).count()
                # if the order doesn't exist, save instance and display in template
                if existing_orders_count < 1:
                    new_order.save()
                    return redirect('calculator:nozzle_orders', nozzle.id)
                # if the order doesn't exist, display error message in template
                else:
                    message = 'Takie zlecenie już istnieje!'
                    context = {'form': form,
                               'message': message,
                               'nozzle':nozzle,
                               'order': order,
                               }
                    template = 'calculator/edit_nozzle_order.html'

                    return render(request, template, context)

    context = {'form': form,
               'nozzle': nozzle,
               'order': order,
               }
    template = 'calculator/edit_nozzle_order.html'

    return render(request, template, context)


def add_nozzle_offer(request, nozzle_id):
    nozzle = Nozzle.objects.get(id=nozzle_id)
    existing_offers_count = 0
    if request.method != 'POST':
        form = OfferForm()
    else:
        form = OfferForm(data=request.POST)
        if form.is_valid():
            new_offer = form.save(commit=False)
            new_offer.nozzle = nozzle
            existing_offers_count = Offer.objects.filter(
                dmcg_offer_number=new_offer.dmcg_offer_number,
                offer_year=new_offer.offer_year).count()
            if existing_offers_count < 1:
                new_offer.save()
                return redirect('calculator:nozzle_offers', nozzle.id)
            else:
                message = 'Taki numer oferty już istnieje!'
                context = {'form': form,
                           'message': message,
                           'nozzle_id': nozzle.id,
                           'nozzle': nozzle,
                           }
                template = 'calculator/add_nozzle_offer.html'

                return render(request, template, context)


    context = {'form': form,
               'nozzle_id': nozzle.id,
               'nozzle': nozzle,
               }
    template = 'calculator/add_nozzle_offer.html'

    return render(request, template, context)


def orders_view(request):
    orders = Order.objects.all()
    orders_filter = OrderFilter(request.GET, queryset=orders)

    orders = orders_filter.qs

    context = {'orders_filter': orders_filter,
               'orders': orders}
    template = 'calculator/orders.html'

    return render(request, template, context)
