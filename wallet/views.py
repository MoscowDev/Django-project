from django.shortcuts import render
from rest_framework import status

from .models import Wallet
from .serializer import WalletTransferSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .services.intra_transfer_service import transfer_wallet_to_wallet
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .serializer import DashboardSerializer


from .services.dashboard_service import get_dashboard_data


# Create your views here.




@api_view(['POST'])
@permission_classes([IsAuthenticated])
def transfer_wallet(request):
    sender = request.user.wallet
    serializer = WalletTransferSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    amount = serializer.validated_data['amount']
    idempotency_key = serializer.validated_data['idempotency_key']
    description = serializer.validated_data['description']
    receiver_wallet = serializer.validated_data['receiver_wallet']
    # description = serializer.Charfield(max_length=400, required=False)

    receiver = get_object_or_404(Wallet, wallet_number = receiver_wallet.pk)
    tx = transfer_wallet_to_wallet(sender, receiver, amount, idempotency_key,description = description)


    return Response(
        {
        'amount': tx.amount,
        'status': tx.status,
        'wallet_number': tx.wallet_number,
        'description': tx.description,
        'reference': tx.reference,
        'created_at': tx.created_at
    }, status =  status.HTTP_201_CREATED

    )

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard(request):
    user = request.user
    dashboard_data = get_dashboard_data(user)
    serializer = DashboardSerializer(dashboard_data)
    return Response(serializer.data, status = status.HTTP_200_OK)