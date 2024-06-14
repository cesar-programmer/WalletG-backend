from django.contrib import admin
from .models import user, profile, account_type, currency, account, fiance_goal, finance_tip, acces_tip

admin.site.register(user)

admin.site.register(profile)
admin.site.register(account_type)
admin.site.register(currency)
admin.site.register(account)
admin.site.register(fiance_goal)
admin.site.register(finance_tip)
admin.site.register(acces_tip)