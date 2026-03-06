from django.core.mail import send_mail
from .models import Notification


# notification/create_wallet_service.py
def create_notification(user):
    notification = Notification.objects.create(
        wallet=user.wallet.wallet_number,
        message=f"""Hi {user.first_name}, welcome to QuickPay!

Your wallet number is: {user.wallet.wallet_number}
Your alternate wallet number is: {user.wallet.account_number}

Thank you for choosing QuickPay!
""",
        event_type="USER_WALLET_CREATED",


    )

    send_mail(
        subject="Welcome to QuickPay!",
        message=notification.message,
        from_email="",
        recipient_list=[user.email],
        fail_silently=True,
    )

    notification.is_read = True
    notification.save()

    # return notification