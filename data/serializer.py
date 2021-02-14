from rest_framework import serializers
from .models import DataDiri
from authentication.models import User

class DataDiriSerializer(serializers.ModelSerializer):
    class Meta:
        model =  DataDiri
        fields=['id','nama_depan', 'nama_belakang', 'kelamin', 'pemilik','umur','kota','alamat','phone', 'bio']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model =  User
        fields=['id','username', 'is_staff', 'is_verified','email']