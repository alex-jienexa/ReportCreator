from rest_framework.decorators import api_view, permission_classes
# Permissions
from rest_framework.permissions import AllowAny, IsAuthenticated
# Serializers
from api.serializers.user import UserSerializer
from api.serializers.company import CompanySerializer
# Response & auth
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import login
# models
from backend.models.company import Executor
from backend.models.user import User

# --- Регистрация компании и суперпользователя ---

@api_view(["POST"])
@permission_classes([AllowAny])
def register_company(request):
    company_name = request.data.get("company_name")
    username = request.data.get("username")
    email = request.data.get("email")
    password = request.data.get("password")
    
    if not all([company_name, username, email, password]):
        return Response(
            {"error": "Нужно заполнение всех полей"},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Создаем компанию
    company = Executor.objects.create(name=company_name)
    
    # Создаем суперпользователя компании
    try:
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            company=company,
            is_superuser_of_company=True,
            is_staff=True  # для доступа к админке если нужно
        )
    except Exception as e:
        company.delete()  # Откатываем создание компании при ошибке
        return Response(
            {"error": str(e)},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Автоматический логин после регистрации
    login(request, user)
    return Response({
        "status": "success",
        "company": CompanySerializer(company).data,
        "user": UserSerializer(user).data
    }, status=status.HTTP_201_CREATED)


# --- Получение информации о компании и пользователях ---

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_company_info(request):
    if not request.user.company:
        return Response(
            {"error": "User has no company"},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    company = request.user.company
    users = User.objects.filter(company=company)
    
    return Response({
        "company": CompanySerializer(company).data,
        "users": UserSerializer(users, many=True).data
    })