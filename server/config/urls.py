from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # setting.py ni import qildik
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

schema_view = get_schema_view(
    openapi.Info(
        title="1 mahalla 2 dasturchi",
        default_version="v1",
        description="binnimade endi",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="google@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("adduser", include("adduser.urls")),
    path("accounts/", include("accounts.urls")),
    path("monitoring/", include("monitoring.urls")),
    path("statistika/", include("statistika.urls")),
    path("excel", include("excell_tables.urls")),
    # API documentation
    path(
        "swagger.<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"
    ),
    path(
        "",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    # JWT
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.STATICFILES_DIRS,
)
