from django.contrib import admin
from .models import Wallet, Transaction, Ledger


# Register your models here.

@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ['wallet_number','account_number','balance', 'currency', 'status']
    list_editable = ['status', 'balance', 'currency']

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
        list_display = [ 'sender', 'receiver', 'amount',  'status']
        list_editable = ['status', 'amount']

@admin.register(Ledger)
class LedgerAdmin(admin.ModelAdmin):
        list_display = ['transaction', 'entry_type', 'amount']
        list_editable = ['entry_type', 'amount']
