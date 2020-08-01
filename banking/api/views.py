from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from personalbanking.models import Customer
from rest_framework.permissions import IsAuthenticated  # <-- Here
from django.core import serializers
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.core.cache import cache
from api.serializers import CustomerSerializer
from banking import settings

from rest_framework.permissions import IsAuthenticated  # <-- Here

class Customers(APIView):
    # permission_classes = (IsAuthenticated,)             # <-- And here

    def get(self, request):
        cache_key = 'AllCustomerReport'  # needs to be unique

        data = cache.get(cache_key)  # returns None if no key-value pair
        # print('---->', settings.CACHE_DURATION)
        # print('---->',data)
        print('---->',cache.key_prefix)

        if not data:
            cust = Customer.objects.all()
            # cache_time = settings.CACHE_DURATION
            data = CustomerSerializer(cust, many=True).data
        cache.set(cache_key, data, settings.CACHE_DURATION)

        return Response(data)

    def post(self,request):
        print(request.query_params)
        acc_num = int(request.query_params.get('acc_num'))
        fname = request.query_params.get('firstname')
        lname = request.query_params.get('lastname')
        branch_id = int(request.query_params.get('branch'))
        # acc_type = request.query_params.get('acc_type')
        try:
            cust1 = Customer(account_number=acc_num, firstname= fname, lastname=lname,
                                    account_type='SB', branch_id=branch_id)
            cust1.save()

        except Exception as e:
            return HttpResponse(st = e, status=500)
        return HttpResponse(status=201)

    def delete(self,request):
        print('--->',request.query_params)
        fname = request.query_params.get('firstname')
        delrec = Customer.objects.filter(firstname__contains=fname).delete()
        return HttpResponse(status=201)
