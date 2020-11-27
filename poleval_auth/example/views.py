from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.conf import settings



@api_view()
@permission_classes([IsAuthenticated])
def hello_world(request):
    print(request.user)
    return Response({"message": "Hello, world!"})


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def create_user(request):
    print(request)
    User = get_user_model()
    secret = request.data['secret']
    if secret == settings.KEYCLOAK_SECRET:
        email = request.data['userData']['email']
        username = request.data['userData']['preferred_username']
        new_user = User.objects.create(email=email, username=username)
    return Response({"user": "created"})


@permission_classes((AllowAny,))
@api_view(['GET', 'POST'])
def user_exists(request):
    User = get_user_model()
    secret = request.data['secret']
    if secret == settings.KEYCLOAK_SECRET:
        email = request.data['email']
        user = get_object_or_404(User, email=email)
    return Response({"message": "user created"})

