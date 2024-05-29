from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import UserInfo
from .serializers import StudentSerializer


class StudentViewSet(ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = StudentSerializer

    def list(self, request, *args, **kwargs):
        users = UserInfo.objects.all()
        serializer = StudentSerializer(users, many=True)
        return Response(serializer.data)
