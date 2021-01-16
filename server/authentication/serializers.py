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
    
    def create(self, validated_data):
        with transaction.atomic():
            type = validated_data.pop("type")
            if 'doctor' in validated_data:
                doctor = validated_data.pop("doctor")
            instance: User = super(UserSerializer, self).create(validated_data)
            if type == "doctor":
                group = Group.objects.get(name="doctor")
                data = doctor
                data.update({"user": instance.id, "spec": data["spec"].id})
                serializer = DoctorHelpSerializer(data=data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
            else:
                group = Group.objects.get(name="client")
            instance.groups.add(group)
            instance.set_password(self.initial_data["password"])
            instance.save()
        return instance

    def update(self, instance, validated_data):
        with transaction.atomic():
            if 'doctor' in validated_data:
                doctor = validated_data.pop("doctor")
            if 'password' in validated_data:
                password = validated_data.pop("password")
            if 'type' in validated_data:
                type = validated_data.pop('type')
            if 'username' in validated_data:
                validated_data.pop('username')
            instance: User = super(UserSerializer, self).update(instance, validated_data)
            if instance.type == "doctor":
                data = doctor
                data.update({"spec": data["spec"].id})
                serializer = DoctorHelpSerializer(instance=instance.doctor, data=data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()

            if password:
                instance.set_password(self.initial_data["password"])
                instance.save()
        return instance