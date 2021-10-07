import logging

from rest_framework import serializers

from app_python.models import User

logger = logging.getLogger(__name__)


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(label='id', read_only=True)
    first_name = serializers.CharField(max_length=32)
    last_name = serializers.CharField(max_length=32)
    gender = serializers.CharField(max_length=10)
    email = serializers.CharField(max_length=255)
    country = serializers.CharField(max_length=32)

    user_category = serializers.CharField(max_length=32)
    role_type = serializers.CharField(max_length=32)
    login_type = serializers.CharField(max_length=32)

    username = serializers.CharField(max_length=255)
    #encoded_password = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)

    secret_question = serializers.CharField(max_length=255)
    encoded_secret_answer = serializers.CharField(max_length=255)
    encoded_custom_secret_question = serializers.CharField(max_length=255)
    encoded_custom_secret_answer = serializers.CharField(max_length=255)

    is_active = serializers.BooleanField()
    is_staff = serializers.BooleanField()

    date_joined = serializers.DateTimeField()
    last_login = serializers.DateTimeField()

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.email = validated_data.get('email', instance.mail)
        instance.country = validated_data.get('country', instance.country)

        instance.user_category = validated_data.get('user_category', instance.user_category)
        instance.role_type = validated_data.get('role_type', instance.role_type)
        instance.login_type = validated_data.get('login_type', instance.login_type)
        instance.username = validated_data.get('username', instance.username)

        #instance.encoded_password = validated_data.get('encoded_password', instance.encoded_password)
        instance.password = validated_data.get('password', instance.password)

        instance.secret_question = validated_data.get('secret_question', instance.secret_question)
        instance.encoded_secret_answer = validated_data.get('encoded_secret_answer', instance.encoded_secret_answer)
        instance.encoded_custom_secret_question = validated_data.get('encoded_custom_secret_question', instance.encoded_custom_secret_question)
        instance.encoded_custom_secret_answer = validated_data.get('encoded_custom_secret_answer', instance.encoded_custom_secret_answer)

        super().update(instance, validated_data)
        return instance

    class Meta:
        fields = ['id',
                  'first_name',
                  'last_name',
                  'gender',
                  'email',
                  'country',
                  'user_category',
                  'role_type',
                  'login_type',
                  'username',
                  'password',
                  'secret_question',
                  'encoded_secret_answer',
                  'encoded_custom_secret_question',
                  'encoded_custom_secret_answer',
                  'is_staff',
                  'is_active',
                  'is_superuser',
                  'date_joined',
                  'last_login',
                  'created_at',
                  'updated_at',
                  ]
        model = User
