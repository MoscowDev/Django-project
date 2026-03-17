from decimal import Decimal
from uuid import UUID
from django.db import transaction
from ..models import Wallet,Transaction,Ledger


def transfer_wallet_to_wallet(
    sender: Wallet,
    receiver: Wallet,
    amount,
    idempotency_key: UUID,
    description: str = None
):
    amount = Decimal(amount)

    if sender.pk == receiver.pk:
        raise Exception("Cannot transfer to self")
    if amount < sender.balance:
        raise Exception("insufficient balance")

    existing_tx = Transaction.objects.filter(
        idempotency_key=idempotency_key
    ).first()

    if existing_tx:
        return existing_tx

    with transaction.atomic():
        receiver_wallet = Wallet.objects.select_for_update().get(pk=receiver.pk)


        sender_wallet = Wallet.objects.select_for_update().get(pk=sender.pk)

        sender_wallet.balance -= amount
        receiver_wallet.balance += amount

        sender_wallet.save(update_fields=["balance"])
        receiver_wallet.save(update_fields=["balance"])

        tx = Transaction.objects.create(
            sender=sender_wallet,
            receiver=receiver_wallet,
            amount=amount,
            idempotency_key=idempotency_key,
            transaction_type="CREDIT",
            status="SUCCESSFUL",
            description=description
        )

        Ledger.objects.create(
            transaction=tx,
            amount=amount,
            wallet=sender_wallet,
            balance_after=sender_wallet.balance,
            entry_type="DEBIT"
        )

        Ledger.objects.create(
            transaction=tx,
            amount=amount,
            wallet=receiver_wallet,
            balance_after=receiver_wallet.balance,
            entry_type="CREDIT"
        )

        return tx