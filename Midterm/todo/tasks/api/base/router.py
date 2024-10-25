from django.urls import path
from tasks.api.base.views import TaskViewSet

urlpatterns = [
    path(
        "tasks/",
        TaskViewSet.as_view({"get": "list", "post": "create"}),
        name="task-list",
    ),
    path(
        "tasks/<int:pk>/",
        TaskViewSet.as_view(
            {
                "get": "retrieve",
                "patch": "partial_update",
                "put": "update",
                "delete": "soft_delete",
            }
        ),
        name="task-detail",
    ),
    path(
        "tasks/<int:pk>/change-priority/",
        TaskViewSet.as_view({"patch": "change_priority"}),
        name="task-change-priority",
    ),
    path(
        "tasks/<int:pk>/change-due-date/",
        TaskViewSet.as_view({"patch": "change_due_date"}),
        name="task-change-due-date",
    ),
    path(
        "tasks/<int:pk>/change-status/",
        TaskViewSet.as_view({"patch": "change_status"}),
        name="task-change-status",
    ),
    path(
        "tasks/<int:pk>/archive/",
        TaskViewSet.as_view({"patch": "archive"}),
        name="task-archive",
    ),
    path(
        "tasks/<int:pk>/unarchive/",
        TaskViewSet.as_view({"patch": "unarchive"}),
        name="task-unarchive",
    ),
    path(
        "tasks/archived/",
        TaskViewSet.as_view({"get": "archived"}),
        name="task-archived",
    ),
]
