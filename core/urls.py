from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView
from django.shortcuts import redirect
from django.urls import path, include, reverse_lazy
from rest_framework.authtoken.views import obtain_auth_token

from utils.auth_view import register

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views as api_views

router = DefaultRouter()
router.register('coffees', api_views.CoffeeViewSet)

urlpatterns = [
    path('coffees/', include('coffees.urls')),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/auth/', obtain_auth_token, name='api_auth'),
]

login_params = {
    'template_name': 'users/login.html',
    'redirect_authenticated_user': True,
}

password_reset_params = {
    'template_name': 'users/password_reset.html',
    'email_template_name': 'users/password_reset/email.html',
    'subject_template_name': 'users/password_reset/subject.txt',
    'success_url': reverse_lazy('login'),
}

password_set_params = {
    'template_name': 'users/password_set.html',
    'post_reset_login': True,
    'success_url': reverse_lazy('login'),
}

urlpatterns = [
    path('', lambda request: redirect('coffees:index'), name='root'),
    path('login/', LoginView.as_view(**login_params), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),

    path(
        'password-reset/',
        PasswordResetView.as_view(**password_reset_params),
        name='password_reset',
    ),
    path(
        'password-set/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(**password_set_params),
        name='password_set',
    ),


    path('coffees/', include('coffees.urls')),
    path('admin/', admin.site.urls),
]
handler403 = 'utils.error_handlers.permission_denied'

