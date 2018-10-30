from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from basesite.models import Car
from basesite.models import Customer
from django.views.decorators.csrf import csrf_exempt

# don't want to use a token to access an api
@csrf_exempt
def carByID(request):
    try:
        id = request.POST
        car = Car.objects.get(id=id['id'])
    # failed to find, sends json
    except Car.DoesNotExist:
        return JsonResponse({'car':'Failed to find'})
    return JsonResponse(car.JSonObject())

# now specifically for the search page. Can specify what to search
@csrf_exempt
def search(request):
    try:
        # Get posted vars
        vals = request.POST
        # Effectively a switch statement to get cars
        if 'selected' in vals:
            if (vals['selected']=='name'):
                car = Car.objects.filter(name__icontains=vals['search'])
            elif (vals['selected']=='model'):
                car = Car.objects.filter(model__icontains=vals['search'])
            elif (vals['selected']=='series'):
                car = Car.objects.filter(series__icontains=vals['search'])
            else:
                car = Car.objects.filter(name__icontains=vals['search'])
        else:
            car = Car.objects.filter(name__icontains=vals['search'])
    except Car.DoesNotExist:
        return JsonResponse({'val': 'failed'})
    # list comprehension -> javascript array
    resp = {'items': [item.JSonObject() for item in car]}
    return JsonResponse(resp)

################################## Customer Search ################################################

@csrf_exempt
def customerByID(request):
    try:
        id = request.POST
        customer = Customer.get(id=id['id'])
    # failed to find, sends json
    except Customer.DoesNotExist:
        return JsonResponse({'customer':'Failed to find'})
    return JsonResponse(customer.JSonObject())

# Seach Specifically for the customers page. Specifies what to search
@csrf_exempt
def customer(request):
    try:
        # Get posted vars
        vals = request.POST
        # Effectively a switch statement to get cars
        if 'selected' in vals:
            if (vals['selected']=='name'):
                customer = Customer.objects.filter(name__icontains=vals['customer'])
            elif (vals['selected']=='birthday'):
                customer = Customer.objects.filter(birthday__icontains=vals['customer'])
            elif (vals['selected']=='address'):
                customer = Customer.objects.filter(address__icontains=vals['customer'])
            else:
                customer = Customer.objects.filter(name__icontains=vals['customer'])
        else:
            customer = Customer.objects.filter(name__icontains=vals['customer'])
    except Customer.DoesNotExist:
        return JsonResponse({'val': 'failed'})
    # list comprehension -> javascript array
    resp = {'items': [item.JSonObject() for item in customer]}
    return JsonResponse(resp)
    
@csrf_exempt
def store(request):
    selectedStore = request.POST
    selectedStore = selectedStore['store']
    car = Car.objects.all()
    # List comprehension to effectively filter for current store
    res = [item.JSonObject() for item in car if selectedStore in item.JSonObject().values()]
    resp = {'cars': res}
    return JsonResponse(resp)

@csrf_exempt
def carHistory(request):
    carID = request.POST['carID']
    car = Car.objects.get(id = carID)
    history = car.history()

    res = [{'pickup_date': order.pickup_date, 'pickup_store': order.pickup_store.name,
    'return_store': order.return_store.name, 'return_date': order.return_date}
    for order in history]

    res = {'history': res}
    return JsonResponse(res)
