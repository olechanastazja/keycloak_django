from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import CustomUser
from .serializers import CustomUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and creating users.
    """

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]
    lookup_field = 'username'


@api_view()
@permission_classes([IsAuthenticated])
def hello_world(request):
    """
    An example view for testing user authentication
    :param request:
    :return: json
    """
    return Response({"message": "Hello, world!"})

