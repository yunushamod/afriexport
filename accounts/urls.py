from unicodedata import name
from django.urls import path, include
from .views import register, edit_profile, get_state_and_countries

urlpatterns = [
    # # login / logout urls
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # dashboard url
    path('', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('edit', edit_profile, name='edit'),
    path('states_and_countries', get_state_and_countries, name='state_and_countries'),
    # password change urls
    # path('password_change/', auth_views.PasswordResetView.as_view(), name='password_change'),
    # path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),
    # # password reset urls
    # path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('password_reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('password_reset/complete', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete')
]