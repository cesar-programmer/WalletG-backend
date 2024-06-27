from django.contrib import admin
from django.urls import path, include
from finance import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', views.user_list),
    path('api/users/<int:id>', views.user_detail),
    path('api/goals/', views.goals_list),
    path('api/goals/<int:id>', views.goals_detail),
    path('api/tips/', views.tips_list),
    path('api/tips/<int:id>', views.tips_detail),
    path('api/account/', views.account_list),
    path('api/account/<int:id>', views.account_detail),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/users/me/', views.current_user, name='current-user'),
    path('api/users/me/profile/', views.current_user_profile, name='current-user-profile'),
    path('api/transactions/', views.create_transaction, name='create_transaction'),

]
