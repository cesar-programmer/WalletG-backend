from django.http import JsonResponse
from .models import User, Profile, Account_type, Currency, Account, Fiance_goal, Finance_tip, Acces_tip, Transaction, Type_transaction
from .serializers import userSerializer, profileSerializer, account_typeSerializer, currencySerializer, accountSerializer, fiance_goalSerializer, finance_tipSerializer, acces_tipSerializer, transactionSerializer, type_transactionSerializer
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authentication import BaseAuthentication
from decimal import Decimal

class NoAuthRequired(BaseAuthentication):
    def authenticate(self, request):
        return None  # To indicate that the user is not authenticated (anonymous user

@api_view(['POST'])
def token_obtain_pair(request):
    user_name = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=user_name, password=password)
    if user:
        return Response({
            "access": user.token,
            "refresh": user.refresh_token
        })
    else:
        print("Failed login attempt", request.data)
        return Response({"detail": "Invalid credentials"}, status=401)

@api_view(['GET', 'POST'])
@authentication_classes([NoAuthRequired])
@permission_classes([AllowAny])
def user_list(request, format=None):
    if request.method == 'GET':
        # Obtén todos los usuarios y sus perfiles asociados
        users  = User.objects.all()
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
@permission_classes([IsAuthenticated])
def user_detail(request, id):
    try:
        users = User.objects.get(id=id)
    except User.DoesNotExist:
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
        User.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def goals_list(request, format=None):
    if request.method == 'GET':
        goals = Fiance_goal.objects.filter(ID_user=request.user)
        serializer = fiance_goalSerializer(goals, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = fiance_goalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def goals_detail(request, id):
    try:
        goals = Fiance_goal.objects.get(ID_goal=id, ID_user=request.user)
    except Fiance_goal.DoesNotExist:
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
@permission_classes([IsAuthenticated])
def tips_list(request, format=None):
    if request.method == 'GET':
        tips = Finance_tip.objects.all()
        serializer = finance_tipSerializer(tips, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = finance_tipSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def tips_detail(request, id):
    try:
        tips = Finance_tip.objects.get(id=id)
    except Finance_tip.DoesNotExist:
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
@permission_classes([IsAuthenticated])
def account_list(request, format=None):
    if request.method == 'GET':
        accounts = Account.objects.filter(ID_user=request.user)
        serializer = accountSerializer(accounts, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = accountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def account_detail(request, id):
    try:
        accounts = Account.objects.get(id=id, ID_user=request.user)
    except Account.DoesNotExist:
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

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):
    # Utiliza el usuario ya autenticado que está adjunto al request
    serializer = userSerializer(request.user)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user_profile(request):
    profile = Profile.objects.get(user=request.user)
    serializer = profileSerializer(profile)
    return Response(serializer.data)

from django.db import transaction

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_transaction(request):
    serializer = transactionSerializer(data=request.data)
    if serializer.is_valid():
        with transaction.atomic():
            account = Account.objects.select_for_update().get(id=serializer.validated_data['ID_account'].id)
            transaction_type = serializer.validated_data['type']
            amount = serializer.validated_data['amount']

            if transaction_type.description.lower() == 'income':
                account.balance += amount
                update_goals_progress(request.user, amount)
            elif transaction_type.description.lower() == 'expense':
                if account.balance >= amount:
                    account.balance -= amount
                    update_goals_progress(request.user, -amount)
                else:
                    return Response({"error": "Insufficient balance"}, status=status.HTTP_400_BAD_REQUEST)

            account.save()
            new_transaction = serializer.save(ID_user=request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def update_goals_progress(user, amount):
    goals = Fiance_goal.objects.filter(ID_user=user, achieved=False)
    for goal in goals:
        new_progress = goal.progress + Decimal(amount)
        
        goal.progress = min(new_progress, goal.amount)
        
        progress_percentage = (goal.progress / goal.amount) * 100
        
        goal.progress_percentage = round(progress_percentage, 2)
        
        if goal.progress >= goal.amount:
            goal.achieved = True
        
        goal.save()


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def transactions_list(request, format=None):
    transactions = Transaction.objects.filter(ID_user=request.user)
    serializer = transactionSerializer(transactions, many=True)
    return JsonResponse(serializer.data, safe=False)