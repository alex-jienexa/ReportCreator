from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login

# --- Работа с аутентификацией пользователей ---

@api_view(["POST"])
def login_view(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(username=username, password=password)
    if user:
        login(request, user)
        return Response({"status": 'success'})
    return Response({"error": 'Invalid error'}, status=400)

@api_view(["GET"])
def get_csrf_token(request):
    from django.middleware.csrf import get_token
    token = get_token(request)
    return Response({"csrf_token": token})

@api_view(["GET"])
def check_auth(request):
    if request.user.is_authenticated:
        return Response({"status": 'authenticated', 'username': request.user.username})
    return Response({"status": 'not_authenticated'}, status=401)