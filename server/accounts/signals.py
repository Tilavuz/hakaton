from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from .models import Maktab, Mahalla


@receiver(pre_save, sender=Maktab)
def check_maktab_overall(sender, instance, **kwargs):
    maktab_overall = (
        instance.plan_en_b2
        + instance.plan_en_a1
        + instance.plan_en_a2
        + instance.plan_ru_b2
        + instance.plan_ru_a1
        + instance.plan_ru_a2
        + instance.plan_deorother_b2
        + instance.plan_deorother_a1
        + instance.plan_deorother_a2
    )
    mahalla_overall = instance.mahalla.overall
    if maktab_overall > mahalla_overall:
        raise ValidationError(
            {"overall": "Sum of maktab plans cannot exceed mahalla overall value"}
        )


@receiver(pre_save, sender=Mahalla)
def check_mahalla_overall(sender, instance, **kwargs):
    mahalla_overall = (
        instance.plan_en_b2
        + instance.plan_en_a1
        + instance.plan_en_a2
        + instance.plan_ru_b2
        + instance.plan_ru_a1
        + instance.plan_ru_a2
        + instance.plan_deorother_b2
        + instance.plan_deorother_a1
        + instance.plan_deorother_a2
    )
    tuman_overall = instance.tuman.overall
    if mahalla_overall > tuman_overall:
        raise ValidationError(
            {"overall": "Sum of mahalla plans cannot exceed tuman overall value"}
        )
