from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser, FormParser
from scratch_bling.api.models import Item
from scratch_bling.api.serializers import ItemSerializer
from rest_framework import viewsets
from .serializers import ItemSerializer
from scratch_bling.api.models import Item
import json


@csrf_exempt
def items_view(request):
    if request.method == 'GET':
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = FormParser().parse(request)
        new_data = data.copy()
        #new_data['item_size'] = json.loads(data['item_size'])
        print(new_data)
        serializer = ItemSerializer(data=new_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def items_detail(request, id):
    try:
        item = Item.objects.get(pk=id)
    except Item.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ItemSerializer(item)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = FormParser().parse(request)
        new_data = data.copy()
        #new_data['item_size'] = json.loads(data['item_size'])
        serializer = ItemSerializer(data=new_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return HttpResponse(status=204)


""" class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
 """
