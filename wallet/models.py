import uuid

from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from .util import generate_account_number, generate_reference_number



# Create your models here.

class Wallet(models.Model):
    CURRENCY_CHOICES = (
    ('NGN', 'Naira'),
    ('USD', 'Dollar'),
    ('EUR', 'Euro'),
    )
    WALLET_STATUS = (
        ('ACTIVE', 'Account is active'),
        ('INACTIVE', 'account is inactive'),
        ('SUSPENDED', 'Account is suspended'),
        ('DEACTIVATED', 'Account is deactivated'),
        ('CLOSED', 'Account is closed'),
        ('FROZEN', 'Account is frozen'),
    )
  
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='wallet')
    wallet_number = models.CharField(max_length = 10,unique = True, primary_key=True)
    account_number = models.CharField(max_length = 10,unique = True, default=generate_account_number())
    balance = models.DecimalField(max_digits=10,decimal_places=2, default= 0.00, null=False)
    currency = models.CharField(max_length = 10,choices = CURRENCY_CHOICES, default='NGN')
    status = models.BooleanField(default = True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f" {self.wallet_number} "



class Transaction(models.Model):
        TRANSACTION_CHOICES = (
        ('DEBIT', 'Debit'),
        ('CREDIT', 'Credit'),
        )
        TRANSACTION_STATUS = (
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
        ('FAILED', 'Failed'),

        )
        # reference_number = models.UUIDField(max_length=100, unique=True, editable=False, blank=False, null=True,default=generate_reference_number())
        reference = models.CharField(max_length = 100 )
        transaction_type = models.CharField(max_length = 6, choices= TRANSACTION_CHOICES, default='DEBIT')
        amount = models.DecimalField(max_digits=10,decimal_places=2)
        sender = models.ForeignKey(Wallet, on_delete=models.PROTECT,related_name='sender')
        receiver = models.ForeignKey(Wallet, on_delete=models.PROTECT,related_name='receiver')
        status = models.CharField(max_length = 100,choices = TRANSACTION_STATUS, default='PENDING')
        description = models.TextField(blank=True)
        created_at = models.DateTimeField(auto_now_add=True)
        idempotency_key = models.UUIDField(unique=True, editable=False, blank=True, null=True)

        def __str__(self):
            return f" {self.reference} "

class Ledger(models.Model):
    TRANSACTION_CHOICES  = (
        ('DEBIT', 'Debit'),
        ('CREDIT', 'Credit'),
    )
    transaction = models.ForeignKey(Transaction, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    balance_after = models.DecimalField(max_digits=10,decimal_places=2)
    wallet = models.ForeignKey(Wallet, on_delete=models.PROTECT)
    entry_type = models.CharField(max_length=100, choices = TRANSACTION_CHOICES, default='DEBIT')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" {self.transaction} {self.entry_type} {self.amount} "