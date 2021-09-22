import datetime
import logging

from rest_framework import serializers

from app_python.models import User

logger = logging.getLogger(__name__)


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(label='id', read_only=True)
    civility = serializers.CharField(max_length=32)
    first_name = serializers.CharField(max_length=32)
    last_name = serializers.CharField(max_length=32)
    gender = serializers.CharField(max_length=10)
    birthday = serializers.DateField(initial=datetime.date.today)
    mail = serializers.CharField(max_length=255)
    city = serializers.CharField(max_length=32)
    country = serializers.CharField(max_length=32)
    phone = serializers.CharField(max_length=32, required=False)

    user_category = serializers.CharField(max_length=32)
    role_type = serializers.CharField(max_length=32)
    login_type = serializers.CharField(max_length=32)
    user_name = serializers.CharField(max_length=255)
    encoded_password = serializers.CharField(max_length=255)
    secret_question = serializers.CharField(max_length=255)
    encoded_secret_answer = serializers.CharField(max_length=255)
    encoded_custom_secret_question = serializers.CharField(max_length=255)
    encoded_custom_secret_answer = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.civility = validated_data.get('civility', instance.civility)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.birthday = validated_data.get('birthday', instance.birthday)
        instance.mail = validated_data.get('mail', instance.mail)
        instance.city = validated_data.get('city', instance.city)
        instance.country = validated_data.get('country', instance.country)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.user_category = validated_data.get('user_category', instance.user_category)
        instance.role_type = validated_data.get('role_type', instance.role_type)
        instance.login_type = validated_data.get('login_type', instance.login_type)
        instance.user_name = validated_data.get('user_name', instance.user_name)
        instance.encoded_password = validated_data.get('encoded_password', instance.encoded_password)
        instance.secret_question = validated_data.get('secret_question', instance.secret_question)
        instance.encoded_secret_answer = validated_data.get('encoded_secret_answer', instance.encoded_secret_answer)
        instance.encoded_custom_secret_question = validated_data.get('encoded_custom_secret_question', instance.encoded_custom_secret_question)
        instance.encoded_custom_secret_answer = validated_data.get('encoded_custom_secret_answer', instance.encoded_custom_secret_answer)

        super().update(instance, validated_data)
        return instance

    class Meta:
        model = User
        fields = ['id',
                  'civility',
                  'first_name',
                  'last_name',
                  'gender',
                  'birthday',
                  'mail',
                  'city',
                  'country',
                  'phone',
                  'user_category',
                  'role_type',
                  'user_name',
                  'login_type',
                  'encoded_password',
                  'secret_question',
                  'encoded_secret_answer',
                  'encoded_custom_secret_question',
                  'encoded_custom_secret_answer',
                  ]
