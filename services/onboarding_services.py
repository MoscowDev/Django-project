# from django.db import transaction
# # from wallet.services import create_wallet
# from user.services import create_user
# from ..notification.models import Notification
# from ..wallet.services.create_wallet_service import create_wallet
# from wallet.notification.models import Notification
# from ..notification.services import create_notification

from django.db import transaction

from user.services import create_user
from wallet.services.create_wallet_service import create_wallet
from notification.models import Notification
from notification.services import create_notification



@transaction.atomic
def create_user_and_wallet(validated_data):
    user = create_user(validated_data)
    wallet = create_wallet(user)
    create_notification(user)
    return user, wallet

