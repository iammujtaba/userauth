from rest_framework import serializers
from api.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name","last_name","username","email","is_email_verified"]
    
    def create(self,validated_data):
        password = validated_data.pop("password",None)
        user = User(**validated_data)
        user.set_password(password)
        return user

    def update(self,validated_data):
        first_name = validated_data.get("first_name")
        last_name = validated_data.get("last_name")
        email = validated_data.get("email")
        user,_ = User.objects.update_or_create(email=email,
                                                defaults = dict(
                                                    first_name = first_name,
                                                    last_name = last_name,
                                                )
                                                )