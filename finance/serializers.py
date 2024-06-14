from rest_framework import serializers
from .models import user, profile, account_type, currency, account, fiance_goal, finance_tip, acces_tip

class userSerializer(serializers.ModelSerializer):
  class Meta:
    model = user
    fields = '__all__'

class profileSerializer(serializers.ModelSerializer):
  class Meta:
    model = profile
    fields = '__all__'

class account_typeSerializer(serializers.ModelSerializer):
  class Meta:
    model = account_type
    fields = '__all__'

class currencySerializer(serializers.ModelSerializer):
  class Meta:
    model = currency
    fields = '__all__'

class accountSerializer(serializers.ModelSerializer):
  class Meta:
    model = account
    fields = '__all__'

class fiance_goalSerializer(serializers.ModelSerializer):
  class Meta:
    model = fiance_goal
    fields = '__all__'

class finance_tipSerializer(serializers.ModelSerializer):
  class Meta:
    model = finance_tip
    fields = '__all__'

class acces_tipSerializer(serializers.ModelSerializer):
  class Meta:
    model = acces_tip
    fields = '__all__'
