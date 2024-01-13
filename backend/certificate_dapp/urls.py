from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('test/', views.testEndPoint, name='test'),
    path('', views.getRoutes),
    path('get_user_detail' , views.get_user_detail),
    path('get_request_list', views.get_request_list),
    path('send_certificate_request', views.send_certificate_request),
    path('user', views.get_all_user_a_wallet),
    path('create_new_nft', views.create_new_nft),
    path('optin_to_asset', views.optin_to_asset),
    path('get_asset_info', views.get_asset_info),
    path('connect', views.connect_to_algo),
    # path('user', get_all_user_a_wallet),
    # path('create_new_nft', create_new_nft),
]