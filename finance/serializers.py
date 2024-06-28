from rest_framework import serializers
from .models import User, Profile, Account_type, Currency, Account, Fiance_goal, Finance_tip, Acces_tip, Transaction, Type_transaction

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'user_name', 'password']

    def create(self, validated_data):
        new_user = User.objects.create_user(
            email=validated_data['email'],
            user_name=validated_data['user_name'],
            password=validated_data['password']
        )
        return new_user

class profileSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profile
    fields = '__all__'

class account_typeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Account_type
    fields = '__all__'

class currencySerializer(serializers.ModelSerializer):
  class Meta:
    model = Currency
    fields = '__all__'

class accountSerializer(serializers.ModelSerializer):
  class Meta:
    model = Account
    fields = '__all__'

class fiance_goalSerializer(serializers.ModelSerializer):
  class Meta:
    model = Fiance_goal
    fields = '__all__'

class finance_tipSerializer(serializers.ModelSerializer):
  class Meta:
    model = Finance_tip
    fields = '__all__'

class acces_tipSerializer(serializers.ModelSerializer):
  class Meta:
    model = Acces_tip
    fields = '__all__'

class transactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['ID_account', 'amount', 'date', 'description', 'type']

class type_transactionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Type_transaction
    fields = '__all__'