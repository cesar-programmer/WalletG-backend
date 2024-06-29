from django.contrib import admin
from .models import User, Profile, Account_type, Currency, Account, Fiance_goal, Finance_tip, Acces_tip, Transaction, Type_transaction
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email', 'user_name')

class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    model = User
    list_display = ['email', 'user_name', 'is_active', 'is_staff', 'is_superuser']
    list_filter = ['is_staff', 'is_superuser', 'is_active']
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser')}
        ),
    )
    search_fields = ('email', 'user_name')
    ordering = ('email',)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('ID_user', 'ID_account', 'amount', 'description', 'date', 'type')

admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)
admin.site.register(Account_type)
admin.site.register(Currency)
admin.site.register(Account)
admin.site.register(Fiance_goal)
admin.site.register(Finance_tip)
admin.site.register(Acces_tip)
admin.site.register(Type_transaction)
