from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.views.decorators.csrf import ensure_csrf_cookie

@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(
        request=request._request,
        username=username,
        password=password
    )

    if user is not None:
        login(request._request, user)

        return Response({
            'message': 'Login successful',
            'username': user.username,
            'is_staff': user.is_staff
        }, status=status.HTTP_200_OK)

    return Response({
        'message': 'Invalid username or password'
    }, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
@ensure_csrf_cookie
def csrf_view(request):
    return Response({'message': 'CSRF cookie set'})