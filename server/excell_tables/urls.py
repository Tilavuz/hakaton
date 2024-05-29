from django.urls import path
from .views import (
    TumanExcelExportView,
    MahallaExcelExportView,
    MaktabExcelExportView,
    UserExcelExportView,
    StatisticsExcelExportView,
    CertificateExcelExportView,
    UserInfoExcelExportView,
    NemesisExcelExportView,
)


urlpatterns = [
    #Excel data for the district
    path(
        "tuman/excel/",
        TumanExcelExportView.as_view(),
        name="tuman_excel_export",
    ),
    #Excel data for neighborhood
    path(
        "mahalla/excel/",
        MahallaExcelExportView.as_view(),
        name="mahalla_excel_export",
    ),
    #Excel data for school
    path(
        "maktab/excel/",
        MaktabExcelExportView.as_view(),
        name="maktab_excel_export",
    ),
    #Excel data for user
    path(
        "user/excel/",
        UserExcelExportView.as_view(),
        name="user_excel_export",
    ),
    #Excel data for statistics
    path(
        "overall-statistics/excel/",
        StatisticsExcelExportView.as_view(),
        name="overall_statistics_excel",
    ),
    path(
        "certificates-uqimoqda/excel/",
        CertificateExcelExportView.as_view(),
        name="certificates_uqimoqda_excel",
    ),
    path(
        "user-info-english/excel/",
        UserInfoExcelExportView.as_view(),
        name="user_info_english_excel",
    ),
    path(
        "user-info-nemesis/excel/",
        NemesisExcelExportView.as_view(),
        name="user_info_nemesis_excel",
    ),
]
