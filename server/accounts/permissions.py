from rest_framework.permissions import BasePermission, IsAdminUser
from django.contrib.auth import get_user_model


User = get_user_model()


class CanCreateLowerRankUser(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if view.action == "create":
                return request.user.rank > User(rank=request.data["rank"]).rank
            return True


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_staff


class IsHokim(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == User.ROLE_HOKIM


class IsHokimYordamchisi(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == User.ROLE_HOKIM_YORDAMCHISI
        )


class IsTumanMasul(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and request.user.role == User.ROLE_TUMAN_MASUL
        )


class IsTumanYoshlarIshlari(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == User.ROLE_TUMAN_YOSHLAR_ISHLARI
        )


class IsMahallaMasul(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == User.ROLE_MAHALLA_MASUL
        )


class IsMahallaYoshlarIshlari(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == User.ROLE_MAHALLA_YOSHLAR_ISHLARI
        )


class IsMaktabMasul(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == User.ROLE_MAKTAB_MASUL
        )


class IsMaktabYoshlarIshlari(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == User.ROLE_MAKTAB_YOSHLAR_ISHLARI
        )
