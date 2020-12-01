from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.conf import settings
from django.http import HttpResponse


@api_view()
@permission_classes([IsAuthenticated])
def hello_world(request):
    print(request.user)
    return Response({"message": "Hello, world!"})


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def create_user(request):
    User = get_user_model()
    client_id = request.data['client_id']
    if client_id == settings['CLIENT_ID']:
        email = request.data['user_data']['email']
        username = request.data['user_data']['preferred_username']
        new_user = User.objects.create(email=email, username=username)
    return Response({"user": "created"})


@permission_classes((AllowAny,))
@api_view(['GET', 'POST'])
def user_exists(request):
    User = get_user_model()
    client_id = request.data['client_id']
    user = None
    if client_id == settings['CLIENT_ID']:
        email = request.data['user_data']['email']
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None
    if user is None:
        return HttpResponse(status=204)
    return Response({"message": "user exists"})


