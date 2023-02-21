from django.utils import timezone
from django.db import models

from config.models import CreationModificationDateBase
from users.models import CustomUser
from tasks.models import Task


class Message(CreationModificationDateBase):
    sender = models.ForeignKey(CustomUser,
                               on_delete=models.CASCADE,
                               related_name='sent_messages'
                               )
    recipient = models.ForeignKey(CustomUser,
                                  on_delete=models.CASCADE,
                                  related_name='received_messages'
                                  )
    subject = models.CharField(max_length=255)
    body = models.TextField()

    class Meta:
        verbose_name_plural = 'Messages'


class MessageRevision(models.Model):
    message = models.ForeignKey(Message,
                                on_delete=models.CASCADE
                                )
    author = models.ForeignKey(CustomUser,
                               on_delete=models.CASCADE
                               )
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
