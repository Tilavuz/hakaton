from django.urls import path
from .views import (
    Tumandone,
    Tumanen,
    Tumannem,
    Mahalladone,
    Mahallaen,
    Mahallanem,
    MahallaListCreateAPIView,
    Maktabdone,
    Maktabnem,
    Maktaben,
    MaktabListCreateAPIView,
    ViloyatListCreateAPIView
)

urlpatterns = [
    # tuman
    path('viloyat', ViloyatListCreateAPIView.as_view(), name='viloyat_info'),
    path("tumandone_info/<int:tuman_id>/", Tumandone.as_view(), name="tumandone"),
    path("tumanen_info/<int:tuman_id>/", Tumanen.as_view(), name="tumanen"),
    path("tumannem_info/<int:tuman_id>/", Tumannem.as_view(), name="tumannem"),
    # mahalla
    path("mahalla_info", MahallaListCreateAPIView.as_view(), name="mahalla_info"),
    path("mahalladone_info/tuman/<int:tuman_id>/mahalla/<int:mahalla_id>/", Mahalladone.as_view(), name="mahalladone"),
    path("mahallaen_info/tuman/<int:tuman_id>/mahalla/<int:mahalla_id>/", Mahallaen.as_view(), name="mahallaen"),
    path("mahallanem_info/tuman/<int:tuman_id>/mahalla/<int:mahalla_id>/", Mahallanem.as_view(), name="mahallanem"),
    # maktba
    path("maktab_info", MaktabListCreateAPIView.as_view(), name="maktab_info"),
    path('maktabdone_info/<int:tuman_id>/mahalla/<int:mahalla_id>/maktab/<int:maktab_id>/', Maktabdone.as_view(), name='maktabdone_info'),
    path("maktaben_info/<int:tuman_id>/mahalla/<int:mahalla_id>/maktab/<int:maktab_id>/", Maktaben.as_view(), name="maktaben"),
    path("maktabnem_info/<int:tuman_id>/mahalla/<int:mahalla_id>/maktab/<int:maktab_id>/", Maktabnem.as_view(), name="maktabnem"),
]
