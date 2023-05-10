from users.models import User
from django.db import models


class Room(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "room"


class RoomJoin(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="roomJoin", db_column="user_id")
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="roomJoin", db_column="room_id")
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "roomJoin"


class Message(models.Model):
    user_id = models.ForeignKey(User, related_name="message", on_delete=models.CASCADE, db_column="user_id")
    room_id = models.ForeignKey(Room, related_name="message", on_delete=models.CASCADE, db_column="room_id")
    message = models.CharField(max_length=512)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "message"

    def __str__(self):
        return self.user_id.email

    def last_30_messages(self, room_id):
        return Message.objects.filter(room_id=room_id).order_by('created_at')[:30]