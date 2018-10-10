from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from basesite.models import Car
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
        vals = request.POST
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
    # list comprehensions are fun
    resp = {'items': [item.JSonObject() for item in car]}
    for item in car:
        print(item.history())
    return JsonResponse(resp)
