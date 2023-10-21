from django.urls import path
from . import views


urlpatterns = [
    path(
        route='verify-email',
        view=views.UserVerifyEmailView.as_view(),
        name='verify',
    ),
    
    path(
        route='profile',
        view=views.UserProfileView.as_view(),
        name='profile',
    ),
    
    path(
        route='reset-password',
        view=views.UserResetPasswordView.as_view(),
        name='reset',
    ),
    
    path(
        route='reset-password-request-sent',
        view=views.UserResetPasswordRequestSentView.as_view(),
        name='reset_sent',
    ),
    
    path(
        route='reset-password-confirm/<uidb64>/<token>',
        view=views.UserResetPasswordConfirm.as_view(),
        name='reset_confirm',
    ),
    
    path(
        route='reset-password-complete',
        view=views.UserResetPasswordCompleteView.as_view(),
        name='reset_complete',
    ),
    
    path(
        route='specifications',
        view=views.UserSpecificationsView.as_view(),
        name='specific',
    ),
    
    path(
        route='activated',
        view=views.UserVerifiedEmailView.as_view(),
        name='verified',
    ),
    
    path(
        route='activate/<uidb64>/<token>',
        view=views.ActivateUserAccount.as_view(),
        name='activate',
    ),
    
    path(
        route='',
        view=views.UserRegisterView.as_view(),
        name='register'
    ),
    
    path(
        route='login',
        view=views.UserLoginView.as_view(),
        name='login',
    ),
    
    path(
        route='logout',
        view=views.UserLogoutView.as_view(),
        name='logout',    
    ),
]