from django.urls import re_path, include

from blog.api.base.router import urlpatterns as api_v1

urlpatterns = [
    re_path("v1/", include(api_v1)),
]
