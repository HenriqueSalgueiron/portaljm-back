from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenRefreshView

from portaljm.accounts.views import (LoginView, UserDetailView,
                                     UserRegistrationView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portaljm.blog.urls')),
    path('login', LoginView.as_view(), name='email_login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserRegistrationView.as_view(), name='user_registration'),
    path('user/', UserDetailView.as_view(), name='user_detail'),

]
