from rest_framework import serializers
from .models import Sender, Notification
from django.db import transaction

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = [
            "title",
            "message",
            "channel",
        ]


class BulkNotificationSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    notifications = NotificationSerializer(many=True)
    def create(self, validated_data):
        notifications_data = validated_data.pop("notifications")

        with transaction.atomic():
            sender = Sender.objects.create(**validated_data)

            notification_objs = [
                Notification(sender=sender, **notification)
                for notification in notifications_data
            ]

            Notification.objects.bulk_create(notification_objs)

        self.created_count = len(notification_objs)

        return sender
        