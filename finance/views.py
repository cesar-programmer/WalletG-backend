from django.http import JsonResponse
from .models import user, profile, account_type, currency, account, fiance_goal, finance_tip, acces_tip
from .serializers import userSerializer, profileSerializer, account_typeSerializer, currencySerializer, accountSerializer, fiance_goalSerializer, finance_tipSerializer, acces_tipSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def user_list(request, format=None):
    if request.method == 'GET':
        users = user.objects.all()
        serializer = userSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        user_data = request.data.get('user')
        profile_data = request.data.get('profile')

        user_serializer = userSerializer(data=user_data)
        if user_serializer.is_valid():
            created_user = user_serializer.save()  # Guarda el usuario y recupera la instancia
            # Ahora crea el perfil asociado a este usuario
            profile_data['user'] = created_user.id  # Asegúrate de asignar el ID del usuario recién creado al perfil
            profile_serializer = profileSerializer(data=profile_data)
            if profile_serializer.is_valid():
                profile_serializer.save()
                return Response({
                    'user': user_serializer.data,
                    'profile': profile_serializer.data
                }, status=status.HTTP_201_CREATED)
            else:
                created_user.delete()  # Elimina el usuario si la creación del perfil falla
                return Response(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, id):

  try:
    users = user.objects.get(id=id)
  except user.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    serializer = userSerializer(users)
    return Response(serializer.data)

  elif request.method == 'PUT':
    serializer = userSerializer(users, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE':
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  


@api_view(['GET', 'POST'])
def goals_list(request, format=None):

  if request.method == 'GET':
    goals = fiance_goal.objects.all()
    serializer = fiance_goalSerializer(goals, many=True)
    return JsonResponse(serializer.data, safe=False)

  elif request.method == 'POST':
    serializer = fiance_goalSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  

@api_view(['GET', 'PUT', 'DELETE'])

def goals_detail(request, id):
  
    try:
      goals = fiance_goal.objects.get(id=id)
    except fiance_goal.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
  
    if request.method == 'GET':
      serializer = fiance_goalSerializer(goals)
      return Response(serializer.data)
  
    elif request.method == 'PUT':
      serializer = fiance_goalSerializer(goals, data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    elif request.method == 'DELETE':
      goals.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET', 'POST'])
def tips_list(request, format=None):

  if request.method == 'GET':
    tips = finance_tip.objects.all()
    serializer = finance_tipSerializer(tips, many=True)
    return JsonResponse(serializer.data, safe=False)

  elif request.method == 'POST':
    serializer = finance_tipSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  

@api_view(['GET', 'PUT', 'DELETE'])

def tips_detail(request, id):
    
      try:
        tips = finance_tip.objects.get(id=id)
      except finance_tip.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
      if request.method == 'GET':
        serializer = finance_tipSerializer(tips)
        return Response(serializer.data)
    
      elif request.method == 'PUT':
        serializer = finance_tipSerializer(tips, data=request.data)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
      elif request.method == 'DELETE':
        tips.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
      
@api_view(['GET', 'POST'])
def account_list(request, format=None):

  if request.method == 'GET':
    accounts = account.objects.all()
    serializer = accountSerializer(accounts, many=True)
    return JsonResponse(serializer.data, safe=False)

  elif request.method == 'POST':
    serializer = accountSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  

@api_view(['GET', 'PUT', 'DELETE'])

def account_detail(request, id):
    try:
      accounts = account.objects.get(id=id)
    except account.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
  
    if request.method == 'GET':
      serializer = accountSerializer(accounts)
      return Response(serializer.data)
  
    elif request.method == 'PUT':
      serializer = accountSerializer(accounts, data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    elif request.method == 'DELETE':
      accounts.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)