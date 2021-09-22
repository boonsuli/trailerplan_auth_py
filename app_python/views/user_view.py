import logging

from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.parsers import JSONParser

from app_python.models import User
from app_python.serializers import UserSerializer

logger = logging.getLogger(__name__)


class UserView(View):

    def get(self, request, user_id):
        logger.info('GET - get user by id='+user_id)
        try:
            user_obj = User.objects.get(pk=int(user_id))
        except User.DoesNotExist:
            return JsonResponse({'message': 'The user does not exist with id=' + user_id},
                                status=status.HTTP_404_NOT_FOUND)

        user_serializer = UserSerializer(user_obj, context={'request': request})
        return JsonResponse(user_serializer.data)

    @csrf_exempt
    def put(self, request, user_id):
        logger.info('PUT - update user by id='+user_id)
        try:
            user_obj = User.objects.get(pk=int(user_id))
        except User.DoesNotExist:
            return JsonResponse({'message': 'The user does not exist with id=' + user_id},
                                status=status.HTTP_404_NOT_FOUND)

        user_data = JSONParser().parse(request)
        logger.info('user to update:')
        logger.info(user_data)
        user_serializer = UserSerializer(user_obj, data=user_data, context={'request': request})

        if user_serializer.is_valid():
            user_serializer.update(user_obj, user_data)
            logger.info('user updated')
            return JsonResponse(user_serializer.data)

        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id):
        logger.info('DELETE - delete user by id='+user_id)
        try:
            user_obj = User.objects.get(pk=int(user_id))
        except User.DoesNotExist:
            return JsonResponse({'message': 'The user does not exist with id=' + user_id},
                                status=status.HTTP_404_NOT_FOUND)
        if user_obj:
            user_obj.delete()
            return JsonResponse({'message': 'user deleted'}, status=status.HTTP_204_NO_CONTENT)

        return JsonResponse({'message': 'Not implemented'}, status=status.HTTP_400_BAD_REQUEST)
