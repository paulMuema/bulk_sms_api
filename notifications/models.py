from django.db import models

class Sender(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Notification(models.Model):
    CHANNEL = [
        ("email", "Email"),
        ("sms", "SMS"),
        ("push", "Push"),
    ]

    title = models.CharField(max_length=255)
    message = models.TextField()
    channel = models.CharField(max_length=20, choices=CHANNEL)
    sender = models.ForeignKey(
        Sender,
        related_name="notifications",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title} ({self.channel})"
