from rest_framework import serializers
from accounts.models import Tuman, Mahalla, Maktab


class TumanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tuman
        fields = (
            "name",
            "overall",
            "done",
            "plan_en_b2",
            "plan_en_c1",
            "plan_deorother_b2",
            "plan_deorother_c1",
        )



class MahallaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mahalla
        fields = (
            "name",
            "tuman",
            "overall",
            "plan_en_b2",
            "plan_en_c1",
            "plan_deorother_b2",
            "plan_deorother_c1",
        )


class MaktabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maktab
        fields = (
            "name",
            "mahalla",
            "overall",
            "plan_en_b2",
            "plan_en_c1",
            "plan_deorother_b2",
            "plan_deorother_c1",
        )
