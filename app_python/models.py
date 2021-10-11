# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import base64
import unicodedata
import logging
from datetime import datetime
from django.contrib.auth.hashers import (
    make_password,
)
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)
from django.db import models

logger = logging.getLogger(__name__)


class UserManager(BaseUserManager):
    """
    Django requires that custom users define their own Manager class. By
    inheriting from `BaseUserManager`, we get a lot of the same code used by
    Django to create a `User`.
    All we have to do is override the `create_user` function which we will use
    to create `User` objects.
    """

    def create_user(self, username, email, password=None):
        """
        Create and return a `User` with an email, username and password.
        """
        if username is None:
            raise TypeError('Users must have a username')

        if email is None:
            raise TypeError('Users must have an email address')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password=None, first_name="first_name", last_name="last_name"):
        """Create and return a `User` with superuser (admin) permissions."""
        if password is None:
            raise TypeError('Superusers must have a password')

        user = self.create_user(username, email, password)
        user.login_type = 'EMAIL'
        user.role_type = 'PRIVILEGED'
        user.user_category = 'ADMIN'
        user.is_superuser = True
        user.is_staff = True
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(name='first_name', db_column='first_name', max_length=32)
    last_name = models.CharField(name='last_name', db_column='last_name', max_length=32)
    gender = models.CharField(name='gender', db_column='gender', max_length=10)
    email = models.EmailField(name='email', db_column='email', max_length=255, unique=True)
    country = models.CharField(name='', db_column='', max_length=32)

    user_category = models.CharField(name='user_category', db_column='user_category', max_length=32, blank=True, null=True)
    role_type = models.CharField(name='role_type', db_column='role_type', max_length=32, blank=True, null=True)
    login_type = models.CharField(name='login_type', db_column='login_type', max_length=32, blank=True, null=True)

    username = models.EmailField(name='username', db_column='username', max_length=255, unique=True)
    password = models.CharField(name='password', db_column='password', max_length=255, blank=True, null=True)

    secret_question = models.CharField(name='secret_question', db_column='secret_question', max_length=255, blank=True, null=True)
    encoded_secret_answer = models.CharField(name='encoded_secret_answer', db_column='encoded_secret_answer', max_length=255, blank=True, null=True)
    encoded_custom_secret_question = models.CharField(name='encoded_custom_secret_question', db_column='encoded_custom_secret_question', max_length=255, blank=True, null=True)
    encoded_custom_secret_answer = models.CharField(name='encoded_custom_secret_answer', db_column='encoded_custom_secret_answer', max_length=255, blank=True, null=True)

    # True if the user is active
    is_active = models.BooleanField(name='is_active', db_column='is_active', default=True)

    # True if the user can access to the admin site
    is_staff = models.BooleanField(name='is_staff', db_column='is_staff', default=False)

    # True if the user have all permission
    is_superuser = models.BooleanField(name='is_superuser', db_column='is_superuser', default=False)

    date_joined = models.DateTimeField(name='date_joined', db_column='date_joined', default=datetime.now)
    last_login = models.DateTimeField(name='last_login', db_column='last_login', default=datetime.now)
    created_at = models.DateTimeField(name='created_at', db_column='created_at', auto_now_add=True)
    updated_at = models.DateTimeField(name='updated_at', db_column='updated_at', auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def token(self):
        """
        Shortcut in order to get the token with 'user.token' instead of user.generate_jwt_token()
        """
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        """
        Generates a JSON Web Token that stores this user's ID and has an expiry
        date set to 60 days into the future.
        """
        dt = datetime.now() + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name + ' - ' + self.username

    def get_short_name(self):
        return self.username

    @classmethod
    def normalize_username(cls, username):
        return unicodedata.normalize('NFKC', username) if isinstance(username, str) else username

    # the password send is encoded in base64
    def check_password(self, password):
        logger.info(f"user '{self.username}' password : {self.password} - password to check: {password}")
        is_correct = super().check_password(base64.b64decode(password))
        if is_correct:
            return True
        else:
            return False

    class Meta:
        managed = False
        db_table = 'user'
