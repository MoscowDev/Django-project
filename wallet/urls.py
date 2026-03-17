from django.urls import path
from .views import transfer_wallet
# from QuickPay.wallet.views import transfer_wallet
from .views import dashboard

urlpatterns = [

    path('transfer/', transfer_wallet, name='transfer'),

    path("dashboard/", dashboard, name="dashboard"),
]