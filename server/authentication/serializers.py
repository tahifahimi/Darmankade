from django.contrib.auth.models import Group
from django.db import transaction
from rest_framework import serializers

from authentication.models import User
from main.models import Spec, Doctor


# HELPER SERIALIZER #
class DoctorHelpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
        read_only_fields = ('user', )
        
    def create(self, validated_data):
        validated_data['user'] = User.objects.get(id=self.initial_data['user'])
        return super(DoctorHelpSerializer, self).create(validated_data)


class UserSerializer(serializers.ModelSerializer):
    type = serializers.CharField(write_only=True)
    doctor = DoctorHelpSerializer(write_only=True, allow_null=True, required=False)
    password = serializers.CharField(allow_null=True, allow_blank=True)

    class Meta:
        model = User
        fields = '__all__'