from django.urls import path
from .views import BulkNotificationView


urlpatterns = [
    path(
        "notifications/bulk/",
        BulkNotificationView.as_view(),
        name="bulk-notifications",
    ),
]