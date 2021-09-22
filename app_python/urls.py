from django.conf.urls import url

from app_python.views.user_view import UserView
from app_python.views.users_view import UsersView

urlpatterns = [
    url(r'^api/users$', UsersView.as_view(), name='user-list'),
    url(r'^api/users/(?P<user_id>[0-9]+)$', UserView.as_view(), name='user-detail'),
]
