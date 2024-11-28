from django.urls import path
from blog.api.notifications_views import notifications_view

urlpatterns = [
    path("", notifications_view, name="notifications"),
]
