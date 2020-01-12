from django.urls import path, include
from accounts.views import SignUp, UserPasswordResetDone, UserPasswordReset, activate, EmailResend

urlpatterns = [
    path('sign_up/', SignUp.as_view(), name='sign_up_url'),
    path('activate/<str:id>/<str:token>/', activate, name='account_activate_url'),
    path('activate/<int:id>/resend/', EmailResend.as_view(), name='account_activate_resend_url'),
    path('password_reset/', UserPasswordReset.as_view(), name='password_reset_url' ),
    path('password_reset_done/', UserPasswordResetDone.as_view(), name='password_reset_done_url'),
    path('', include('django.contrib.auth.urls')),
]