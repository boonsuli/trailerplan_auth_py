import logging

from django.http import JsonResponse
from django.views import View
from rest_framework import status
from rest_framework.parsers import JSONParser

from app_python.models import User

logger = logging.getLogger(__name__)


class AuthSigninView(View):
    def post(self, request):
        auth_data = JSONParser().parse(request)
        if auth_data:
            username = auth_data.get('username')
            encoded_password = auth_data.get('encodedPassword')
            user_obj = User.objects.filter(user_name=username).get()
            logger.info('POST - signin username=' + username + ' encoded_password=' + encoded_password)

            if user_obj:
                if user_obj.encoded_password == encoded_password:

                    return JsonResponse({'message': 'authenticated'}, status=status.HTTP_200_OK)
                else:
                    return JsonResponse({'message': 'invalid password'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return JsonResponse({'message': 'user not found'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return JsonResponse({'message': 'credential expected'}, status=status.HTTP_400_BAD_REQUEST)

        return JsonResponse({'status': 'ok'}, status=status.HTTP_200_OK)
