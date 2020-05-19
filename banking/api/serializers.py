from rest_framework import serializers
from personalbanking.models import Customer


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ('account_number', 'firstname', 'lastname','branch', 'loan')
