import logging

from django.http import JsonResponse
from django.views import View
from rest_framework import status
from rest_framework.parsers import JSONParser

from app_python.serializers import UserSerializer

logger = logging.getLogger(__name__)


class AuthSignupView(View):
    def post(self, request):
        user_data = JSONParser().parse(request)
        logger.info('POST - signup user to create:')
        logger.info(user_data)
        user_serializer = UserSerializer(data=user_data, context={'request': request})

        if user_serializer.is_valid():
            user_serializer.save()
            logger.info('user created')
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED)

        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
