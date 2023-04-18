from django.contrib.auth import get_user_model
from .models import UserAdditionalInfo


def user_additional_info(request):
    user = request.user
    user_additional_info = None
    if user.is_authenticated:
        try:
            user_additional_info = UserAdditionalInfo.objects.get(username=user)
        except UserAdditionalInfo.DoesNotExist:
            pass
    print("----------", user_additional_info)
    return {'user_additional_info': user_additional_info}
