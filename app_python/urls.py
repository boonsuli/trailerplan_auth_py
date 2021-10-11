from django.conf.urls import url

from app_python.views.auth_signin_view import AuthSigninView
from app_python.views.auth_signup_view import AuthSignupView
from app_python.views.user_view import UserView
from app_python.views.users_view import UsersView

urlpatterns = [
    url(r'^trailerplan/api/auth/signin$', AuthSigninView.as_view(), name='auth-signin'),
    url(r'^trailerplan/api/auth/signup$', AuthSignupView.as_view(), name='auth-signup'),
    url(r'^trailerplan/api/users$', UsersView.as_view(), name='user-list'),
    url(r'^trailerplan/api/users/(?P<user_id>[0-9]+)$', UserView.as_view(), name='user-detail'),
]
