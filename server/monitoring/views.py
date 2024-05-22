from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum, Count, Q
from accounts.models import Tuman, Mahalla, Maktab
from accounts.permissions import (
    IsAdmin,
    IsHokim,
    IsHokimYordamchisi,
)
from adduser.models import UserInfo, Certificate
from adduser.serializers import StudentSerializer, CertificateSerializer
from accounts.serializers import TumanSerializer, MahallaSerializer, MaktabSerializer


class StatisticsView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin | IsHokim | IsHokimYordamchisi]

    def get(self, request):
        total_tuman = Tuman.objects.count()
        total_mahalla = Mahalla.objects.count()
        total_maktab = Maktab.objects.count()

        total_plan_en_b2 = Tuman.objects.aggregate(Sum("plan_en_b2"))["plan_en_b2__sum"]
        total_plan_en_c1 = Tuman.objects.aggregate(Sum("plan_en_c1"))["plan_en_c1__sum"]
        total_plan_en_c2 = Tuman.objects.aggregate(Sum("plan_en_c2"))["plan_en_c2__sum"]
        total_plan_deorother_b2 = Tuman.objects.aggregate(Sum("plan_deorother_b2"))[
            "plan_deorother_b2__sum"
        ]
        total_plan_deorother_c1 = Tuman.objects.aggregate(Sum("plan_deorother_c1"))[
            "plan_deorother_c1__sum"
        ]
        total_plan_deorother_c2 = Tuman.objects.aggregate(Sum("plan_deorother_c2"))[
            "plan_deorother_c2__sum"
        ]

        return Response(
            {
                "total_tuman": total_tuman,
                "total_mahalla": total_mahalla,
                "total_maktab": total_maktab,
                "total_plan_en_b2": total_plan_en_b2,
                "total_plan_en_c1": total_plan_en_c1,
                "total_plan_en_c2": total_plan_en_c2,
                "total_plan_deorother_b2": total_plan_deorother_b2,
                "total_plan_deorother_c1": total_plan_deorother_c1,
                "total_plan_deorother_c2": total_plan_deorother_c2,
            }
        )


class SearchView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin | IsHokim | IsHokimYordamchisi]

    def get(self, request):
        query = request.query_params.get("query", "")
        tuman_queryset = Tuman.objects.filter(name__icontains=query)
        mahalla_queryset = Mahalla.objects.filter(name__icontains=query)
        maktab_queryset = Maktab.objects.filter(name__icontains=query)

        tuman_serializer = TumanSerializer(tuman_queryset, many=True)
        mahalla_serializer = MahallaSerializer(mahalla_queryset, many=True)
        maktab_serializer = MaktabSerializer(maktab_queryset, many=True)

        return Response(
            {
                "tuman": tuman_serializer.data,
                "mahalla": mahalla_serializer.data,
                "maktab": maktab_serializer.data,
            }
        )


class MonitoringView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin | IsHokim | IsHokimYordamchisi]

    def get(self, request):
        tuman_queryset = Tuman.objects.all()
        mahalla_queryset = Mahalla.objects.all()
        maktab_queryset = Maktab.objects.all()

        tuman_serializer = TumanSerializer(tuman_queryset, many=True)
        mahalla_serializer = MahallaSerializer(mahalla_queryset, many=True)
        maktab_serializer = MaktabSerializer(maktab_queryset, many=True)

        return Response(
            {
                "tuman": tuman_serializer.data,
                "mahalla": mahalla_serializer.data,
                "maktab": maktab_serializer.data,
            }
        )


class OrderingView(ModelViewSet):
    permission_classes = [IsAuthenticated, IsAdmin | IsHokim | IsHokimYordamchisi]
    serializer_class = TumanSerializer

    def get_queryset(self):
        queryset = Tuman.objects.all()
        order_by = self.request.query_params.get("order_by", "name")
        order_direction = self.request.query_params.get("order_direction", "asc")

        if order_direction == "desc":
            order_by = f"-{order_by}"

        return queryset.order_by(order_by)


class UserInfoStatisticsView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin | IsHokim | IsHokimYordamchisi]

    def get(self, request):
        total_users = UserInfo.objects.count()
        total_certificates = Certificate.objects.count()
        certificates_by_lang = Certificate.objects.values("title").annotate(
            count=Count("title")
        )
        certificates_by_level = Certificate.objects.values("overel").annotate(
            count=Count("overel")
        )

        return Response(
            {
                "total_users": total_users,
                "total_certificates": total_certificates,
                "certificates_by_lang": certificates_by_lang,
                "certificates_by_level": certificates_by_level,
            }
        )


class UserInfoSearchView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin | IsHokim | IsHokimYordamchisi]

    def get(self, request):
        query = request.query_params.get("query", "")
        user_info_queryset = UserInfo.objects.filter(
            Q(name__icontains=query)
            | Q(lastname__icontains=query)
            | Q(fname__icontains=query)
            | Q(school__icontains=query)
            | Q(neighborhood__icontains=query)
            | Q(JSHSHIR__icontains=query)
            | Q(phone_number__icontains=query)
        )
        serializer = StudentSerializer(user_info_queryset, many=True)
        return Response(serializer.data)


class UserInfoOrderingView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin | IsHokim | IsHokimYordamchisi]

    def get(self, request):
        order_by = request.query_params.get("order_by", "name")
        order_direction = request.query_params.get("order_direction", "asc")

        if order_direction == "desc":
            order_by = f"-{order_by}"

        user_info_queryset = UserInfo.objects.order_by(order_by)
        serializer = StudentSerializer(user_info_queryset, many=True)
        return Response(serializer.data)


class CertificateMonitoringView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin | IsHokim | IsHokimYordamchisi]

    def get(self, request):
        certificate_queryset = Certificate.objects.all()
        serializer = CertificateSerializer(certificate_queryset, many=True)
        return Response(serializer.data)
