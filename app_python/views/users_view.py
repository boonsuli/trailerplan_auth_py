import logging

from django.http import JsonResponse
from django.views import View
from rest_framework import status
from rest_framework.parsers import JSONParser

from app_python.models import User
from app_python.serializers import UserSerializer

logger = logging.getLogger(__name__)


class UsersView(View):

    def get(self, request, *args, **kwargs):
        logger.info('GET - get list of users')
        users = User.objects.order_by('id')
        users_serializer = UserSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)

    def post(self, request, *args, **kwargs):
        user_data = JSONParser().parse(request)
        logger.info('POST - user to create:')
        logger.info(user_data)
        user_serializer = UserSerializer(data=user_data, context={'request': request})

        if user_serializer.is_valid():
            user_serializer.save()
            logger.info('user created')
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED)

        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        return JsonResponse({'message': 'Not implemented'}, status=status.HTTP_400_BAD_REQUEST)
