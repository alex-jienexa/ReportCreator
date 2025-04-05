from rest_framework import serializers
from backend.models import User
from backend.models.fields import Field
from .company import CompanySerializer

class UserSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    
    class Meta:
        model = User
        fields = [
            'id', 'username', 
            'company', 'is_superuser_of_company',
            'first_name', 'last_name', 'patronymic',
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user

class UserFieldSerializer(serializers.ModelSerializer):
    type = serializers.ChoiceField(choices=Field.FIELD_TYPES)

    class Meta:
        model = Field
        fields = '__all__'