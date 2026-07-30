from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import BulkNotificationSerializer


class BulkNotificationView(APIView):
    def post(self, request):
        serializer = BulkNotificationSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        sender = serializer.save()

        return Response(
            {
                "message": "Notifications created successfully.",
                "sender_id": sender.id,
                "notifications_created": serializer.created_count,
            },
            status=status.HTTP_201_CREATED,
        )