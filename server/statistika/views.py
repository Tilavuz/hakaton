from rest_framework import generics, status
from accounts.models import Tuman, Maktab, Mahalla,Viloyat
from accounts.serializers import MahallaSerializer, MaktabSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from adduser.models import Certificate,UserInfo
from accounts.serializers import ViloyatSerializer
from accounts.permissions import (
    IsAdmin,
    IsHokim,
    IsHokimYordamchisi,
    IsTumanMasul,
    IsTumanYoshlarIshlari,
    IsMahallaMasul,
    IsMahallaYoshlarIshlari,
    IsMaktabMasul,
    IsMaktabYoshlarIshlari,
)

# Tuman


class Tumandone(APIView):
    permission_classes = [
        IsAuthenticated,
        IsAdmin | IsHokim | IsHokimYordamchisi | IsTumanMasul | IsTumanYoshlarIshlari,
    ]

    def get(self, request, tuman_id):
        try:
            tuman = Tuman.objects.get(id=tuman_id)
        except Tuman.DoesNotExist:
            return Response({"error": "Tuman not found"}, status=status.HTTP_404_NOT_FOUND)

        eng_start = Certificate.objects.filter(
            user_info__status="uqimoqda", 
            title="english"
        ).count()
        eng_end = Certificate.objects.filter(
            user_info__status="tugatgan", 
            title="english"
        ).count()
        all_en = tuman.plan_en_b2 + tuman.plan_en_c1
        enuqimoqda = round((eng_start / all_en * 100), 1) if all_en != 0 else 0
        entugatgan = round((eng_end / all_en * 100), 1) if all_en != 0 else 0

        nem_start = Certificate.objects.filter(
            user_info__status="uqimoqda", 
            title="nemesis"
        ).count()
        nem_end = Certificate.objects.filter(
            user_info__status="tugatgan", 
            title="nemesis"
        ).count()
        all_nem = (tuman.plan_deorother_c1 + tuman.plan_deorother_b2) / 100
        nemuqimoqda = round((nem_start / all_nem * 100), 1) if all_nem != 0 else 0
        nemtugatgan = round((nem_end / all_nem * 100), 1) if all_nem != 0 else 0

        all_uqimoqda = nem_start + eng_start

        return Response(
            {
                "tuman_name": tuman.name,
                "all_uqimoqda": all_uqimoqda,
                "tuman_done": all_en,
                "eng_uqimoqda": eng_start,
                "eng_uqimoqda_percent": enuqimoqda,
                "eng_tugatgan": eng_end,
                "eng_tugatgan_percent": entugatgan,
                "nem_uqimoqda": nem_start,
                "nem_uqimoqda_percent": nemuqimoqda,
                "nem_tugatgan": nem_end,
                "nem_tugatgan_percent": nemtugatgan,
            },
            status=status.HTTP_200_OK,
        )

class Tumanen(APIView):
    permission_classes = [
        IsAuthenticated,
        IsAdmin | IsHokim | IsHokimYordamchisi | IsTumanMasul | IsTumanYoshlarIshlari,
    ]

    def get(self, request, tuman_id):
        try:
            tuman = Tuman.objects.get(id=tuman_id)
        except Tuman.DoesNotExist:
            return Response({"error": "Tuman not found"}, status=status.HTTP_404_NOT_FOUND)

        all_paln_en = tuman.plan_en_c1 + tuman.plan_en_b2

        all_en = Certificate.objects.filter(
            user_info__status="uqimoqda",
            title="english",
            overel__in=["B2", "C1"],
        ).count()

        percent = round((all_en / all_paln_en * 100), 1) if all_paln_en != 0 else 0

        en_end = Certificate.objects.filter(
            user_info__status="tugatgan",
            title="english",
            overel__in=["B2", "C1"],
        ).count()

        en_percent = round((en_end / all_paln_en * 100), 1) if all_paln_en != 0 else 0

        en_b2_start = Certificate.objects.filter(
            user_info__status="uqimoqda",
            title="english",
            overel="B2"
        ).count()

        en_b2_end = Certificate.objects.filter(
            user_info__status="tugatgan",
            title="english", 
            overel="B2"
        ).count()

        en_c1_start = Certificate.objects.filter(
            user_info__status="uqimoqda", 
            title="english", 
            overel="C1"
        ).count()

        en_c1_end = Certificate.objects.filter(
            user_info__status="tugatgan", 
            title="english", 
            overel="C1"
        ).count()

        return Response(
            {
                "tuman_name": tuman.name,
                "all_plan": all_paln_en,
                "all_en": all_en,
                "all_en_percent": percent,
                "en_sertifikat": en_end,
                "en_end_percent": en_percent,
                "en_b2_start": en_b2_start,
                "en_b2_end": en_b2_end,
                "en_c1_start": en_c1_start,
                "en_c1_end": en_c1_end,
            },
            status=status.HTTP_200_OK,
        )

class Tumannem(APIView):
    permission_classes = [
        IsAuthenticated,
        IsAdmin | IsHokim | IsHokimYordamchisi | IsTumanMasul | IsTumanYoshlarIshlari,
    ]

    def get(self, request, tuman_id):
        try:
            tuman = Tuman.objects.get(id=tuman_id)
        except Tuman.DoesNotExist:
            return Response({"error": "Tuman not found"}, status=status.HTTP_404_NOT_FOUND)

        all_paln_en = tuman.plan_en_c1 + tuman.plan_en_b2

        all_nem = Certificate.objects.filter(
            user_info__status="uqimoqda",
            title="nemesis",
            overel__in=["B2", "C1"],
        ).count()

        percent = round((all_nem / all_paln_en * 100), 1) if all_paln_en != 0 else 0

        nem_end = Certificate.objects.filter(
            user_info__status="tugatgan",
            title="nemesis",
            overel__in=["B2", "C1"],
        ).count()

        nem_percent = round((nem_end / all_paln_en * 100), 1) if all_paln_en != 0 else 0

        nem_b2_start = Certificate.objects.filter(
            user_info__status="uqimoqda", 
            title="nemesis", 
            overel="B2"
        ).count()

        nem_b2_end = Certificate.objects.filter(
            user_info__status="tugatgan", 
            title="nemesis", 
            overel="B2"
        ).count()

        nem_c1_start = Certificate.objects.filter(
            user_info__status="uqimoqda", 
            title="nemesis", 
            overel="C1"
        ).count()

        nem_c1_end = Certificate.objects.filter(
            user_info__status="tugatgan", 
            title="nemesis", 
            overel="C1"
        ).count()

        return Response(
            {
                "tuman_name": tuman.name,
                "all_plan": all_paln_en,
                "all_nem": all_nem,
                "all_nem_percent": percent,
                "nem_sertifikat": nem_end,
                "nem_end_percent": nem_percent,
                "nem_b2_start": nem_b2_start,
                "nem_b2_end": nem_b2_end,
                "nem_c1_start": nem_c1_start,
                "nem_c1_end": nem_c1_end,
            },
            status=status.HTTP_200_OK,
        )

class ViloyatListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [
        IsAuthenticated,
        IsAdmin | IsHokim | IsHokimYordamchisi | IsTumanMasul | IsTumanYoshlarIshlari,
    ]
    queryset = Viloyat.objects.all()
    serializer_class = ViloyatSerializer


# Mahalla


class Mahalladone(APIView):
    permission_classes = [
        IsAuthenticated,
        IsAdmin | IsHokim | IsHokimYordamchisi | IsTumanMasul | IsTumanYoshlarIshlari | IsMahallaMasul | IsMahallaYoshlarIshlari,
    ]

    def get(self, request, mahalla_id, tuman_id):
        try:
            mahalla = Mahalla.objects.get(id=mahalla_id, tuman_id=tuman_id)
        except Mahalla.DoesNotExist:
            return Response({"error": "Mahalla not found"}, status=status.HTTP_404_NOT_FOUND)

        eng_start = Certificate.objects.filter(
            user_info__status="uqimoqda",
            user_info__tuman=tuman_id,
            title="english",
        ).count()
        eng_end = Certificate.objects.filter(
            user_info__status="tugatgan",
            user_info__tuman=tuman_id,
            title="english",
        ).count()
        all_en = mahalla.plan_en_b2 + mahalla.plan_en_c1
        enuqimoqda = round((eng_start / all_en * 100), 1) if all_en != 0 else 0
        entugatgan = round((eng_end / all_en * 100), 1) if all_en != 0 else 0

        nem_start = Certificate.objects.filter(
            user_info__status="uqimoqda",
            user_info__tuman=tuman_id,
            title="nemesis",
        ).count()
        nem_end = Certificate.objects.filter(
            user_info__status="tugatgan",
            user_info__tuman=tuman_id,
            title="nemesis",
        ).count()
        all_nem = (mahalla.plan_deorother_c1 + mahalla.plan_deorother_b2) / 100
        nemuqimoqda = round((nem_start / all_nem * 100), 1) if all_nem != 0 else 0
        nemtugatgan = round((nem_end / all_nem * 100), 1) if all_nem != 0 else 0

        all_uqimoqda = nem_start + eng_start

        return Response(
            {   
                "tuman": mahalla.tuman.name,
                "mahalla_name": mahalla.name,
                "all_uqimoqda": all_uqimoqda,
                "mahalla_done": all_en,
                "eng_uqimoqda": eng_start,
                "eng_uqimoqda_percent": enuqimoqda,
                "eng_tugatgan": eng_end,
                "eng_tugatgan_percent": entugatgan,
                "nem_uqimoqda": nem_start,
                "nem_uqimoqda_percent": nemuqimoqda,
                "nem_tugatgan": nem_end,
                "nem_tugatgan_percent": nemtugatgan,
            },
            status=status.HTTP_200_OK,
        )

class Mahallaen(APIView):
    permission_classes = [
        IsAuthenticated,
        IsAdmin | IsHokim | IsHokimYordamchisi | IsTumanMasul | IsTumanYoshlarIshlari | IsMahallaMasul | IsMahallaYoshlarIshlari,
    ]

    def get(self, request,tuman_id, mahalla_id):
        try:
            mahalla = Mahalla.objects.get(id=mahalla_id, tuman_id=tuman_id)
        except Mahalla.DoesNotExist:
            return Response({"error": "Mahalla not found"}, status=status.HTTP_404_NOT_FOUND)

        all_paln_en = mahalla.plan_en_c1 + mahalla.plan_en_b2

        all_en = Certificate.objects.filter(
            user_info__status="uqimoqda",
            user_info__tuman=tuman_id,
            title="english",
            overel__in=["B2", "C1"],
        ).count()
        percent = round((all_en / all_paln_en * 100), 1) if all_paln_en != 0 else 0

        en_end = Certificate.objects.filter(
            user_info__status="tugatgan",
            user_info__tuman=tuman_id,
            title="english",
            overel__in=["B2", "C1"],
        ).count()
        en_percent = round((en_end / all_paln_en * 100), 1) if all_paln_en != 0 else 0

        en_b2_start = Certificate.objects.filter(
            user_info__status="uqimoqda", title="english", overel="B2",user_info__tuman=tuman_id,
        ).count()
        en_b2_end = Certificate.objects.filter(
            user_info__status="tugatgan", title="english", overel="B2",user_info__tuman=tuman_id,
        ).count()
        en_c1_start = Certificate.objects.filter(
            user_info__status="uqimoqda", title="english", overel="C1",user_info__tuman=tuman_id,
        ).count()
        en_c1_end = Certificate.objects.filter(
            user_info__status="tugatgan", title="english", overel="C1",user_info__tuman=tuman_id,
        ).count()

        return Response(
            {   
                "tuman": mahalla.tuman.name,
                "mahalla_name": mahalla.name,
                "all_plan": all_paln_en,
                "all_en": all_en,
                "all_en_percent": percent,
                "en_sertifikat": en_end,
                "en_end_percent": en_percent,
                "en_b2_start": en_b2_start,
                "en_b2_end": en_b2_end,
                "en_c1_start": en_c1_start,
                "en_c1_end": en_c1_end,
            },
            status=status.HTTP_200_OK,
        )

class Mahallanem(APIView):
    permission_classes = [
        IsAuthenticated,
        IsAdmin | IsHokim | IsHokimYordamchisi | IsTumanMasul | IsTumanYoshlarIshlari | IsMahallaMasul | IsMahallaYoshlarIshlari,
    ]

    def get(self, request, mahalla_id, tuman_id):
        try:
            mahalla = Mahalla.objects.get(id=mahalla_id, tuman_id=tuman_id)
        except Mahalla.DoesNotExist:
            return Response({"error": "Mahalla not found"}, status=status.HTTP_404_NOT_FOUND)

        all_paln_en = mahalla.plan_en_c1 + mahalla.plan_en_b2

        all_nem = Certificate.objects.filter(
            user_info__status="uqimoqda",
            user_info__tuman=tuman_id,
            title="nemesis",
            overel__in=["B2", "C1"],
        ).count()
        percent = round((all_nem / all_paln_en * 100), 1) if all_paln_en != 0 else 0

        nem_end = Certificate.objects.filter(
            user_info__status="tugatgan",
            user_info__tuman=tuman_id,
            title="nemesis",
            overel__in=["B2", "C1"],
        ).count()
        nem_percent = round((nem_end / all_paln_en * 100), 1) if all_paln_en != 0 else 0

        nem_b2_start = Certificate.objects.filter(
            user_info__status="uqimoqda", title="nemesis", overel="B2",user_info__tuman=tuman_id,
        ).count()
        nem_b2_end = Certificate.objects.filter(
            user_info__status="tugatgan", title="nemesis", overel="B2",user_info__tuman=tuman_id,
        ).count()
        nem_c1_start = Certificate.objects.filter(
            user_info__status="uqimoqda", title="nemesis", overel="C1",user_info__tuman=tuman_id,
        ).count()
        nem_c1_end = Certificate.objects.filter(
            user_info__status="tugatgan", title="nemesis", overel="C1",user_info__tuman=tuman_id,
        ).count()

        return Response(
            {   
                "tuman": mahalla.tuman.name,
                "mahalla_name": mahalla.name,
                "all_plan": all_paln_en,
                "all_nem": all_nem,
                "all_nem_percent": percent,
                "nem_sertifikat": nem_end,
                "nem_end_percent": nem_percent,
                "nem_b2_start": nem_b2_start,
                "nem_b2_end": nem_b2_end,
                "nem_c1_start": nem_c1_start,
                "nem_c1_end": nem_c1_end,
            },
            status=status.HTTP_200_OK,
        )

class MahallaListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [
        IsAuthenticated,
        IsAdmin | IsHokim | IsHokimYordamchisi | IsTumanMasul | IsTumanYoshlarIshlari | IsMahallaMasul | IsMahallaYoshlarIshlari,
    ]

    queryset = Mahalla.objects.all()
    serializer_class = MahallaSerializer
# maktab

class Maktabdone(APIView):
    permission_classes = [
        IsAuthenticated,
        IsAdmin | IsHokim | IsHokimYordamchisi | IsTumanMasul | IsTumanYoshlarIshlari |
        IsMahallaMasul | IsMahallaYoshlarIshlari | IsMaktabMasul | IsMaktabYoshlarIshlari,
    ]

    def get(self, request,tuman_id, mahalla_id, maktab_id):
        try:
            maktab = Maktab.objects.get(id=maktab_id, mahalla_id=mahalla_id, tuman_id=tuman_id)
        except Maktab.DoesNotExist:
            return Response({"error": "Maktab not found"}, status=status.HTTP_404_NOT_FOUND)

        eng_start = Certificate.objects.filter(
            user_info__status="uqimoqda",
            user_info__school_id=maktab_id,
            user_info__neighborhood_id=mahalla_id,
            user_info__tuman_id=tuman_id,
            title="english",
        ).count()
        eng_end = Certificate.objects.filter(
            user_info__status="tugatgan",
            user_info__school_id=maktab_id,
            user_info__neighborhood_id=mahalla_id,
            user_info__tuman_id=tuman_id,
            title="english",
        ).count()
        all_en = maktab.overall
        enuqimoqda = round((eng_start / all_en * 100), 1) if all_en != 0 else 0
        entugatgan = round((eng_end / all_en * 100), 1) if all_en != 0 else 0

        nem_start = Certificate.objects.filter(
            user_info__status="uqimoqda",
            user_info__school_id=maktab_id,
            user_info__neighborhood_id=mahalla_id,
            user_info__tuman_id=tuman_id,
            title="nemesis",
        ).count()
        nem_end = Certificate.objects.filter(
            user_info__status="tugatgan",
            user_info__school_id=maktab_id,
            user_info__neighborhood_id=mahalla_id,
            user_info__tuman_id=tuman_id,
            title="nemesis",
        ).count()
        all_nem = (maktab.plan_deorother_c1 + maktab.plan_deorother_b2) / 100
        nemuqimoqda = round((nem_start / all_nem * 100), 1) if all_nem != 0 else 0
        nemtugatgan = round((nem_end / all_nem * 100), 1) if all_nem != 0 else 0

        all_uqimoqda = nem_start + eng_start

        return Response(
            {   
                "tuman": maktab.mahalla.tuman.name,
                "mahalla": maktab.mahalla.name,
                "maktab_name": maktab.name,
                "all_uqimoqda": all_uqimoqda,
                "maktab_done": all_en,
                "eng_uqimoqda": eng_start,
                "eng_uqimoqda_percent": enuqimoqda,
                "eng_tugatgan": eng_end,
                "eng_tugatgan_percent": entugatgan,
                "nem_uqimoqda": nem_start,
                "nem_uqimoqda_percent": nemuqimoqda,
                "nem_tugatgan": nem_end,
                "nem_tugatgan_percent": nemtugatgan,
            },
            status=status.HTTP_200_OK,
        )


class Maktaben(APIView):
    permission_classes = [
        IsAuthenticated,
        IsAdmin | IsHokim | IsHokimYordamchisi | IsTumanMasul | IsTumanYoshlarIshlari | IsMahallaMasul | IsMahallaYoshlarIshlari | IsMaktabMasul | IsMaktabYoshlarIshlari,
    ]

    def get(self, request,tuman_id, mahalla_id, maktab_id):
        try:
            maktab = Maktab.objects.get(id=maktab_id, mahalla_id=mahalla_id, tuman_id=tuman_id)
        except Maktab.DoesNotExist:
            return Response({"error": "Maktab not found"}, status=status.HTTP_404_NOT_FOUND)

        all_plan_en = maktab.plan_en_c1 + maktab.plan_en_b2

        all_en = Certificate.objects.filter(
            user_info__status="uqimoqda",
            title="english",
            user_info__school_id=maktab_id,
            user_info__neighborhood_id=mahalla_id,
            user_info__tuman_id=tuman_id,
            overel__in=["B2", "C1"],
        ).count()
        percent = round(((all_en / all_plan_en) * 100), 1) if all_plan_en != 0 else 0

        en_end = Certificate.objects.filter(
            user_info__status="tugatgan",
            title="english",
            user_info__school_id=maktab_id,
            user_info__neighborhood_id=mahalla_id,
            user_info__tuman_id=tuman_id,
            overel__in=["B2", "C1"],
        ).count()
        en_percent = round(((en_end / all_plan_en) * 100), 1) if all_plan_en != 0 else 0

        en_b2_start = Certificate.objects.filter(
            user_info__school_id=maktab_id,
            user_info__neighborhood_id=mahalla_id,
            user_info__tuman_id=tuman_id,
            user_info__status="uqimoqda", title="english", overel="B2"
        ).count()
        en_b2_end = Certificate.objects.filter(
            user_info__school_id=maktab_id,
            user_info__neighborhood_id=mahalla_id,
            user_info__tuman_id=tuman_id,
            user_info__status="tugatgan", title="english", overel="B2"
        ).count()
        en_c1_start = Certificate.objects.filter(
            user_info__school_id=maktab_id,
            user_info__neighborhood_id=mahalla_id,
            user_info__tuman_id=tuman_id,
            user_info__status="uqimoqda", title="english", overel="C1"
        ).count()
        en_c1_end = Certificate.objects.filter(
            user_info__school_id=maktab_id,
            user_info__neighborhood_id=mahalla_id,
            user_info__tuman_id=tuman_id,
            user_info__status="tugatgan", title="english", overel="C1"
        ).count()

        return Response(
            {   
                
                "maktab_name": maktab.name,
                "all_plan": all_plan_en,
                "all_en": all_en,
                "all_en_percent": percent,
                "en_sertifikat": en_end,
                "en_end_percent": en_percent,
                "en_b2_start": en_b2_start,
                "en_b2_end": en_b2_end,
                "en_c1_start": en_c1_start,
                "en_c1_end": en_c1_end,
            },
            status=status.HTTP_200_OK,
        )

    
class Maktabnem(APIView):
    permission_classes = [
        IsAuthenticated,
        IsAdmin | IsHokim | IsHokimYordamchisi | IsTumanMasul | IsTumanYoshlarIshlari | IsMahallaMasul | IsMahallaYoshlarIshlari | IsMaktabMasul | IsMaktabYoshlarIshlari,
    ]

    def get(self, request,tuman_id, mahalla_id, maktab_id):
        try:
            maktab = Maktab.objects.get(id=maktab_id , mahalla_id=mahalla_id, tuman_id=tuman_id)
        except Maktab.DoesNotExist:
            return Response({"error": "Maktab not found"}, status=status.HTTP_404_NOT_FOUND)

        all_plan_en = maktab.plan_en_c1 + maktab.plan_en_b2

        all_nem = Certificate.objects.filter(
            user_info__school_id=maktab_id,
            user_info__neighborhood_id=mahalla_id,
            user_info__tuman_id=tuman_id,
            user_info__status="uqimoqda", title="nemesis", overel__in=["B2", "C1"],
        ).count()
        percent = round((all_nem / all_plan_en * 100), 1) if all_plan_en != 0 else 0

        nem_end = Certificate.objects.filter(
            user_info__school_id=maktab_id,
            user_info__neighborhood_id=mahalla_id,
            user_info__tuman_id=tuman_id,
            user_info__status="tugatgan", title="nemesis", overel__in=["B2", "C1"],
        ).count()
        nem_percent = round((nem_end / all_plan_en * 100), 1) if all_plan_en != 0 else 0

        nem_b2_start = Certificate.objects.filter(
            user_info__school_id=maktab_id,
            user_info__neighborhood_id=mahalla_id,
            user_info__tuman_id=tuman_id,
            user_info__status="uqimoqda", title="nemesis", overel="B2"
        ).count()
        nem_b2_end = Certificate.objects.filter(
            user_info__school_id=maktab_id,
            user_info__neighborhood_id=mahalla_id,
            user_info__tuman_id=tuman_id,
            user_info__status="tugatgan", title="nemesis", overel="B2"
        ).count()
        nem_c1_start = Certificate.objects.filter(
            user_info__school_id=maktab_id,
            user_info__neighborhood_id=mahalla_id,
            user_info__tuman_id=tuman_id,
            user_info__status="uqimoqda", title="nemesis", overel="C1"
        ).count()
        nem_c1_end = Certificate.objects.filter(
            user_info__school_id=maktab_id,
            user_info__neighborhood_id=mahalla_id,
            user_info__tuman_id=tuman_id,
            user_info__status="tugatgan", title="nemesis", overel="C1"
        ).count()

        return Response(
            {   
                "tuman": maktab.mahalla.tuman.name,
                "mahalla": maktab.mahalla.name,
                "maktab_name": maktab.name,
                "all_plan": all_plan_en,
                "all_nem": all_nem,
                "all_nem_percent": percent,
                "nem_sertifikat": nem_end,
                "nem_end_percent": nem_percent,
                "nem_b2_start": nem_b2_start,
                "nem_b2_end": nem_b2_end,
                "nem_c1_start": nem_c1_start,
                "nem_c1_end": nem_c1_end,
            },
            status=status.HTTP_200_OK,
        )


class MaktabListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [
        IsAuthenticated,
        IsAdmin | IsHokim | IsHokimYordamchisi | IsTumanMasul | IsTumanYoshlarIshlari | IsMahallaMasul | IsMahallaYoshlarIshlari | IsMaktabMasul | IsMaktabYoshlarIshlari,
    ]
    queryset = Maktab.objects.all()
    serializer_class = MaktabSerializer