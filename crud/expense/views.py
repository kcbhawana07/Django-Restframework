from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Transaction
from rest_framework.response import Response
from .serializers import TransactionSerializer
# Create your views here.

@api_view()
def get_transaction(request):
    queryset=Transaction.objects.all()
    serializer=TransactionSerializer(queryset,many='True')

    return Response({
        "data":serializer.data
    })
