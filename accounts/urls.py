from django.urls import path
from accounts.views import SignUp, ChangeUserDetails, ChangeUserDetailsDone

urlpatterns = [
    path('sign_up/', SignUp.as_view(), name='sign_up_url'),
    path('password_reset/', ChangeUserDetails.as_view(), name='password_reset_url' ),
    path('password_reset_done/', ChangeUserDetailsDone.as_view(), name='password_reset_done_url')
]