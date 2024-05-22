from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    StatisticsView,
    SearchView,
    MonitoringView,
    OrderingView,
    StatisticsView,
    SearchView,
    MonitoringView,
    OrderingView,
    UserInfoStatisticsView,
    UserInfoSearchView,
    UserInfoOrderingView,
    CertificateMonitoringView,
)


router = DefaultRouter()
router.register(r"tuman", OrderingView, basename="tuman")

urlpatterns = [
    path("statistics/", StatisticsView.as_view(), name="statistics"),
    path("search/", SearchView.as_view(), name="search"),
    path("monitoring/", MonitoringView.as_view(), name="monitoring"),
    path(
        "user-info-statistics/",
        UserInfoStatisticsView.as_view(),
        name="user-info-statistics",
    ),
    path("user-info-search/", UserInfoSearchView.as_view(), name="user-info-search"),
    path(
        "user-info-ordering/", UserInfoOrderingView.as_view(), name="user-info-ordering"
    ),
    path(
        "certificate-monitoring/",
        CertificateMonitoringView.as_view(),
        name="certificate-monitoring",
    ),
    path("", include(router.urls)),
]
