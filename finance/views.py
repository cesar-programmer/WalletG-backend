from django.http import JsonResponse
from .models import user, profile, account_type, currency, account, fiance_goal, finance_tip, acces_tip
from .serializers import userSerializer, profileSerializer, account_typeSerializer, currencySerializer, accountSerializer, fiance_goalSerializer, finance_tipSerializer, acces_tipSerializer


def user_list(request):
  users = user.objects.all()
  serializer = userSerializer(users, many=True)
  return JsonResponse(serializer.data, safe=False)