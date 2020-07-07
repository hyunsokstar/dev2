from rest_framework import serializers
from django.contrib.auth import get_user_model 

User = get_user_model()

class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True) # 비밀번호는 쓰기 전용 설정을 해야 디비로부터 비번을 읽어오지 않는다.

    # 비밀 번호 암호화에서 저장하도록 create 함수 커스터 마이징 (set_password 함수를 통해 저장해야 함)
    def create(self, validated_data):
        user = User.objects.create(username=validated_data["username"])
        user.set_password(validated_data["password"])
        user.save()
        return user

    class Meta:
        model = User
        fields = ['pk', 'username', 'password']
