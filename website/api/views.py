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
        # apparently request object is a generator so i need to call next to get the value
        car = Car.objects.get(id=next(id.values()))

    # failed to find, sends json
    except Car.DoesNotExist:
        return JsonResponse({'car':'Failed to find'})

    return JsonResponse(car.JSonObject())
