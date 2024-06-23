from rest_framework import serializers
from .models import User, Profile, Account_type, Currency, Account, Fiance_goal, Finance_tip, Acces_tip

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # Make sure the model is also capitalized in the models.py
        # estos son los campos que se van a serializar y devolver en la respuesta
        fields = ['id', 'email', 'user_name', 'password']

    def create(self, validated_data):
        # Using 'new_user' as the variable name to avoid shadowing the 'User' model
        # esta función se ejecuta cuando se llama a serializer.save() en la vista
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
