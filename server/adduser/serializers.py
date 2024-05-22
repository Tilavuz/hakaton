from rest_framework import serializers
from .models import UserInfo, Certificate


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ["overel", "url", "serticatedate"]


class StudentSerializer(serializers.ModelSerializer):
    certificates = CertificateSerializer(many=True)

    class Meta:
        model = UserInfo
        fields = [
            "id",
            "name",
            "lastname",
            "fname",
            "image",
            "school",
            "neighborhood",
            "tuman",
            "title",
            "JSHSHIR",
            "phone_number",
            "userdate",
            "certificates",
            "status",
        ]

    def create(self, validated_data):
        certificates_data = validated_data.pop("certificates")
        jshshir = validated_data.pop("JSHSHIR")

        try:
            student = UserInfo.objects.get(JSHSHIR=jshshir)
            created = False
        except UserInfo.DoesNotExist:
            student = UserInfo.objects.create(**validated_data, JSHSHIR=jshshir)
            created = True

        for certificate_data in certificates_data:
            Certificate.objects.create(user_info=student, **certificate_data)

        return student
