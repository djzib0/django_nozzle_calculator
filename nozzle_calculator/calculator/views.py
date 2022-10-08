from django.shortcuts import render, redirect
from django.db.models import Count, Sum, F
from .models import Nozzle, Order, Offer, NozzleCalculation, AdditionalNozzleHours
from .forms import NozzleForm, OrderForm, OfferForm, AdditionalNozzleHoursForm
from .filters import NozzleFilter, OrderFilter, OfferFilter

from .functions import translate_type_name, calculate_nozzle_welding_material_and_hours

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
    nozzle_total_calculations = NozzleCalculation.objects.filter(nozzle=nozzle).count()
    nozzle_total_orders = Order.objects.filter(nozzle=nozzle).count()
    nozzle_total_offers = Offer.objects.filter(nozzle=nozzle).count()

    context = {'nozzle': nozzle,
               'ratio': ratio,
               'type_name': type_name,
               'nozzle_total_orders': nozzle_total_orders,
               'nozzle_total_offers': nozzle_total_offers,
               'nozzle_id': nozzle_id,
               'nozzle_total_calculations': nozzle_total_calculations,
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
    ratio = round((nozzle.profile_height / nozzle.diameter), 1)

    context = {'nozzle': nozzle,
               'offers': offers,
               'ratio': ratio,
               }
    template = 'calculator/nozzle-offers.html'

    return render(request, template, context)


def nozzle_calculations_view(request, nozzle_id):
    nozzle = Nozzle.objects.get(id=nozzle_id)
    ratio = round((nozzle.profile_height / nozzle.diameter), 1)
    calculations = nozzle.nozzlecalculation_set.order_by('date_created').annotate(
        total_additional_hours=Sum(F('additionalnozzlehours__additional_hours_amount'))).annotate(
        total_hours=F('assembly_hours') + F('welding_hours') + F('spinning_hours') + F('small_machining_hours')
            + F('medium_machining_hours') + F('tos_machining_hours') + F('cutting_plates_hours')
            + F('bending_hours') + F('rolling_profiles_hours'))

    for calculation in calculations:
        print(calculation.total_hours)

    template = 'calculator/nozzle_calculations.html'
    context = {'nozzle': nozzle,
               'calculations': calculations,
               'ratio': ratio,
               # 'total_additional_hours': total_additional_hours,
               }

    return render(request, template, context)


def nozzle_calculation_details_view(request, nozzle_id, calculation_id):
    nozzle = Nozzle.objects.get(id=nozzle_id)
    ratio = round((nozzle.profile_height / nozzle.diameter), 1)
    calculation = NozzleCalculation.objects.get(id=calculation_id)
    total_hours = (calculation.assembly_hours + calculation.welding_hours + calculation.spinning_hours
                   + calculation.spinning_hours + calculation.small_machining_hours
                   + calculation.medium_machining_hours + calculation.tos_machining_hours
                   + calculation.cutting_plates_hours + calculation.bending_hours
                   + calculation.rolling_profiles_hours)

    additional_nozzle_hours = calculation.additionalnozzlehours_set.order_by('group')

    additional_hours = AdditionalNozzleHours.objects.filter(calculation=calculation).aggregate(total_hours=Sum('additional_hours_amount'))

    try:
        sum_of_all_hours = additional_hours['total_hours'] + total_hours
    except:
        sum_of_all_hours = total_hours

    additional_assembly_hours = AdditionalNozzleHours.objects.filter(
        calculation=calculation, group='assembly_hours').\
        aggregate(total_hours=Sum('additional_hours_amount'))
    try:
        all_assembly_hours = additional_assembly_hours['total_hours'] + calculation.assembly_hours
    except:
        all_assembly_hours = calculation.assembly_hours

    additional_welding_hours = AdditionalNozzleHours.objects.filter(
        calculation=calculation, group='welding_hours').\
        aggregate(total_hours=Sum('additional_hours_amount'))
    try:
        all_welding_hours = additional_welding_hours['total_hours'] + calculation.welding_hours
    except:
        all_welding_hours = calculation.welding_hours

    additional_spinning_hours = AdditionalNozzleHours.objects.filter(
        calculation=calculation, group='spinning_hours').\
        aggregate(total_hours=Sum('additional_hours_amount'))
    try:
       all_spinning_hours = additional_spinning_hours['total_hours'] + calculation.spinning_hours
    except:
        all_spinning_hours = calculation.spinning_hours

    additional_small_machining_hours = AdditionalNozzleHours.objects.filter(
        calculation=calculation, group='small_machining_hours'). \
        aggregate(total_hours=Sum('additional_hours_amount'))
    try:
        all_small_machining_hours = additional_small_machining_hours['total_hours'] + calculation.small_machining_hours
    except:
        all_small_machining_hours = calculation.small_machining_hours

    additional_medium_machining_hours = AdditionalNozzleHours.objects.filter(
        calculation=calculation, group='medium_machining_hours'). \
        aggregate(total_hours=Sum('additional_hours_amount'))
    try:
        all_medium_machining_hours = additional_medium_machining_hours['total_hours'] + calculation.medium_machining_hours
    except:
        all_medium_machining_hours = calculation.medium_machining_hours

    additional_tos_machining_hours = AdditionalNozzleHours.objects.filter(
        calculation=calculation, group='tos_machining_hours'). \
        aggregate(total_hours=Sum('additional_hours_amount'))
    try:
        all_tos_machining_hours = additional_tos_machining_hours['total_hours'] + calculation.tos_machining_hours
    except:
        all_tos_machining_hours = calculation.tos_machining_hours

    additional_cutting_plates_hours = AdditionalNozzleHours.objects.filter(
        calculation=calculation, group='cutting_plates_hours'). \
        aggregate(total_hours=Sum('additional_hours_amount'))
    try:
        all_cutting_plates_hours = additional_cutting_plates_hours['total_hours'] + calculation.cutting_plates_hours
    except:
        all_cutting_plates_hours = calculation.cutting_plates_hours

    additional_bending_hours = AdditionalNozzleHours.objects.filter(
        calculation=calculation, group='bending__hours'). \
        aggregate(total_hours=Sum('additional_hours_amount'))
    try:
        all_bending_hours = additional_bending_hours['total_hours'] + calculation.bending_hours
    except:
        all_bending_hours = calculation.bending_hours

    additional_rolling_profiles_hours = AdditionalNozzleHours.objects.filter(
        calculation=calculation, group='rolling_profiles_hours'). \
        aggregate(total_hours=Sum('additional_hours_amount'))
    try:
        all_rolling_profiles_hours = additional_rolling_profiles_hours['total_hours'] + calculation.rolling_profiles_hours
    except:
        all_rolling_profiles_hours = calculation.rolling_profiles_hours


    context = {'calculation': calculation,
               'nozzle': nozzle,
               'ratio': ratio,
               'additional_nozzle_hours': additional_nozzle_hours,
               'total_hours': total_hours,
               'additional_hours': additional_hours,
               'sum_of_all_hours': sum_of_all_hours,
               'all_assembly_hours': all_assembly_hours,
               'all_welding_hours': all_welding_hours,
               'all_spinning_hours': all_spinning_hours,
               'all_small_machining_hours': all_small_machining_hours,
               'all_medium_machining_hours': all_medium_machining_hours,
               'all_tos_machining_hours': all_tos_machining_hours,
               'all_cutting_plates_hours': all_cutting_plates_hours,
               'all_bending_hours': all_bending_hours,
               'all_rolling_profiles_hours': all_rolling_profiles_hours
               }
    template = 'calculator/nozzle_calculation_details.html'

    return render(request, template, context)


def add_nozzle_calculation_view(request, nozzle_id):
    nozzle = Nozzle.objects.get(id=nozzle_id)
    test_result = calculate_nozzle_welding_material_and_hours(nozzle)
    type_name = translate_type_name(str(nozzle.inner_ring_type))

    if request.method == 'POST':
        new_calculation = NozzleCalculation(nozzle=nozzle,
                                            welding_hours=test_result,
                                            # tutaj dodać parametry i wyniki z funkcji
                                            # np.assembly_hours
                                            diameter=nozzle.diameter,
                                            profile=nozzle.profile,
                                            drawing_number=nozzle.drawing_number,
                                            profile_height=nozzle.profile_height,
                                            inner_ring_type=nozzle.inner_ring_type,
                                            inner_ring_thickness_propeller_zone=nozzle.inner_ring_thickness_propeller_zone,
                                            inner_ring_thickness_inlet_zone=nozzle.inner_ring_thickness_inlet_zone,
                                            inner_ring_thickness_outlet_zone=nozzle.inner_ring_thickness_outlet_zone,
                                            ribs_quantity=nozzle.ribs_quantity,
                                            ribs_thickness=nozzle.ribs_thickness,
                                            segments_quantity=nozzle.segments_quantity,
                                            segments_thickness=nozzle.segments_thickness,
                                            has_headbox=nozzle.has_headbox,
                                            has_outlet_ring=nozzle.has_outlet_ring,
                                            theoretical_weight=nozzle.theoretical_weight,
                                            real_weight=nozzle.real_weight,
                                            )
        new_calculation.save()
        return redirect('calculator:nozzle_calculations', nozzle.id)

    context = {'test_result': test_result,
               'nozzle': nozzle,
               'type_name': type_name,
               }
    template = 'calculator/add_nozzle_calculation.html'

    return render(request, template, context)


def add_additional_nozzle_hour(request, nozzle_id, calculation_id,):
    nozzle = Nozzle.objects.get(id=nozzle_id)
    calculation = NozzleCalculation.objects.get(id=calculation_id)

    if request.method != 'POST':
        form = AdditionalNozzleHoursForm()
    else:
        form = AdditionalNozzleHoursForm(request.POST)
        if form.is_valid():
            new_additional_nozzle_hours = form.save(commit=False)
            new_additional_nozzle_hours.calculation = calculation
            new_additional_nozzle_hours = form.save()
            return redirect('calculator:nozzle_calculation_details', nozzle.id, calculation.id)

    context = {'form': form,
               'nozzle': nozzle,
               'calculation': calculation,
               }
    template = 'calculator/add_additional_nozzle_hours.html'

    return render(request, template, context)


def edit_additional_nozzle_hours(request, nozzle_id, calculation_id, additional_nozzle_hour_id):
    nozzle = Nozzle.objects.get(id=nozzle_id)
    calculation = NozzleCalculation.objects.get(id=calculation_id)
    additional_nozzle_hours = AdditionalNozzleHours.objects.get(id=additional_nozzle_hour_id)

    if request.method != 'POST':
        form = AdditionalNozzleHoursForm(instance=additional_nozzle_hours)
    else:
        form = AdditionalNozzleHoursForm(instance=additional_nozzle_hours, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('calculator:nozzle_calculation_details', nozzle_id, calculation_id)

    context = {'form': form,
               'nozzle': nozzle,
               'calculation': calculation,
               'additional_nozzle_hours': additional_nozzle_hours
               }
    template = 'calculator/edit_additional_nozzle_hours.html'

    return render(request, template, context)


def delete_additional_nozzle_hours(request, nozzle_id, calculation_id, additional_nozzle_hour_id):
    nozzle = Nozzle.objects.get(id=nozzle_id)
    calculation = NozzleCalculation.objects.get(id=calculation_id)
    additional_nozzle_hours = AdditionalNozzleHours.objects.get(id=additional_nozzle_hour_id)

    if request.method == 'POST':
        additional_nozzle_hours.delete()
        return redirect('calculator:nozzle_calculation_details', nozzle_id, calculation_id)

    context = {'nozzle': nozzle,
               'calculation': calculation,
               'additional_nozzle_hours': additional_nozzle_hours,
               }
    template = 'calculator/delete_additional_nozzle_hours.html'
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
    ratio = round((nozzle.profile_height / nozzle.diameter), 1)
    if request.method != 'POST':
        form = NozzleForm(instance=nozzle)
    else:
        form = NozzleForm(instance=nozzle, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('calculator:nozzle_details', nozzle.id)

    context = {'form': form,
               'nozzle': nozzle,
               'ratio': ratio}
    template = 'calculator/edit_nozzle.html'

    return render(request, template, context)


def add_nozzle_order(request, nozzle_id):
    nozzle = Nozzle.objects.get(id=nozzle_id)
    ratio = round((nozzle.profile_height / nozzle.diameter), 1)

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
                           'ratio': ratio,
                           }
                template = 'calculator/add_nozzle_order.html'

                return render(request, template, context)

    context = {'form': form,
               'nozzle_id': nozzle.id,
               'nozzle': nozzle,
               'ratio': ratio,
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
                # if the order exists, display error message in template
                else:
                    message = 'Takie zlecenie już istnieje!'
                    context = {'form': form,
                               'message': message,
                               'nozzle': nozzle,
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
    ratio = round((nozzle.profile_height / nozzle.diameter), 1)
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
                           'ratio': ratio,
                           }
                template = 'calculator/add_nozzle_offer.html'

                return render(request, template, context)

    context = {'form': form,
               'nozzle_id': nozzle.id,
               'nozzle': nozzle,
               'ratio': ratio,
               }
    template = 'calculator/add_nozzle_offer.html'

    return render(request, template, context)


def edit_nozzle_offer(request, nozzle_id, offer_id):
    nozzle = Nozzle.objects.get(id=nozzle_id)
    offer = Offer.objects.get(id=offer_id)
    existing_dmcg_offer_number = offer.dmcg_offer_number
    existing_offer_year = offer.offer_year

    if request.method != 'POST':
        form = OfferForm(instance=offer)
    else:
        form = OfferForm(instance=offer, data=request.POST)
        if form.is_valid():
            new_offer = form.save(commit=False)
            # existing offer is the same (no change from user)
            if new_offer.dmcg_offer_number == existing_dmcg_offer_number and \
                    new_offer.offer_year == existing_offer_year:
                return redirect('calculator:nozzle_offers', nozzle.id)
            # if the offer is different, first check whether it already exists
            else:
                existing_offers_count = Offer.objects.filter(
                    dmcg_offer_number=new_offer.dmcg_offer_number,
                    offer_year=new_offer.offer_year).count()
                # if the offer doesn't exist, save instance and display in template
                if existing_offers_count < 1:
                    new_offer.save()
                    return redirect('calculator:nozzle_offers', nozzle.id)
                # if the offer exists, display error message in template
                else:
                    message = 'Taki numer oferty już istnieje!'
                    context = {'form': form,
                               'message': message,
                               'nozzle': nozzle,
                               'offer': offer,
                               }
                    template = 'calculator/edit_nozzle_offer.html'

                    return render(request, template, context)

    context = {'form': form,
               'nozzle': nozzle,
               'offer': offer,
               }
    template = 'calculator/edit_nozzle_offer.html'

    return render(request, template, context)


def orders_view(request):
    orders = Order.objects.all()
    orders_filter = OrderFilter(request.GET, queryset=orders)

    orders = orders_filter.qs

    context = {'orders_filter': orders_filter,
               'orders': orders}
    template = 'calculator/orders.html'

    return render(request, template, context)


def offers_view(request):
    offers = Offer.objects.all()
    offers_filter = OfferFilter(request.GET, queryset=offers)

    offers = offers_filter.qs

    context = {'offers': offers,
               'offers_filter': offers_filter,
               }
    template = 'calculator/offers.html'

    return render(request, template, context)
