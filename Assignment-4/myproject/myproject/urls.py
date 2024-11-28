"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken import views as drf_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from blog.api import notifications_router, router_v1, router_v2

api_v1_patterns = [
    path("api/v1/", include((router_v1, "api_v1"), namespace="api_v1")),
    path(
        "api/v1/api-token-auth/", drf_views.obtain_auth_token, name="api-token-auth-v1"
    ),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

api_v2_patterns = [
    path("api/v2/", include((router_v2, "api_v2"), namespace="api_v2")),
    path(
        "api/v2/api-token-auth/", drf_views.obtain_auth_token, name="api-token-auth-v2"
    ),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

notifications_patterns = [
    path(
        "notifications/",
        include(
            (notifications_router.urlpatterns, "notifications"),
            namespace="notifications",
        ),
    ),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    *api_v1_patterns,
    *api_v2_patterns,
    *notifications_patterns,
]

if settings.DEBUG:
    from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

    urlpatterns += [
        path(
            "api/schema/v1/",
            SpectacularAPIView.as_view(urlconf=api_v1_patterns),
            name="schema-v1",
        ),
        path(
            "api/schema/v1/swagger-ui/",
            SpectacularSwaggerView.as_view(url_name="schema-v1"),
            name="swagger-ui-v1",
        ),
    ]

    urlpatterns += [
        path(
            "api/schema/v2/",
            SpectacularAPIView.as_view(urlconf=api_v2_patterns),
            name="schema-v2",
        ),
        path(
            "api/schema/v2/swagger-ui/",
            SpectacularSwaggerView.as_view(url_name="schema-v2"),
            name="swagger-ui-v2",
        ),
    ]
