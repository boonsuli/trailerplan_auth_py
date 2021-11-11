import logging

import json
import simplejson
from django.http import JsonResponse
from django.views import View
from django.core.serializers import serialize
from rest_framework import status
from rest_framework.parsers import JSONParser
from base64 import b64decode
from django.contrib.auth.hashers import (
    check_password, is_password_usable, make_password,
)
from rest_framework_jwt.views import JSONWebTokenAPIView
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from app_python.models import User
from rest_framework_jwt.utils import jwt_response_payload_handler

logger = logging.getLogger(__name__)


class AuthSigninView(JSONWebTokenAPIView):
    serializer_class = JSONWebTokenSerializer

    def post(self, request):
        client_auth_data = JSONParser().parse(request)
        if client_auth_data:
            username = client_auth_data.get('username')
            encoded_password = client_auth_data.get('encoded_password')
            user_obj = User.objects.filter(username=username).get()
            logger.info(f"POST - signin username={username} encoded_password={encoded_password}")

            if user_obj:
                if user_obj.check_password(encoded_password):
                    auth_data = {"username": username, "password": encoded_password, "email": user_obj.email}
                    serializer = super().get_serializer(data=auth_data)
                    if serializer.is_valid():
                        token = serializer.object.get('token')
                        response_data = jwt_response_payload_handler(token, user_obj, request)
                        user_json = serialize("json", [user_obj])
                        user_struct = json.loads(user_json)
                        data = user_struct[0]['fields']

                        return JsonResponse({"token": response_data.get('token'), "user": data},
                                            status=status.HTTP_200_OK)
                else:
                    return JsonResponse({'message': 'invalid password'}, status=status.HTTP_401_UNAUTHORIZED)
            else:
                return JsonResponse({'message': 'user not found'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return JsonResponse({'message': 'credential expected'}, status=status.HTTP_400_BAD_REQUEST)

        return JsonResponse({'status': 'ok'}, status=status.HTTP_200_OK)
