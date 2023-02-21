from django.db import models
from project.models import Project
from tasks.models import Task, Comment
from messaging.models import Message


class CalendarEvent(models.Model):
    title = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField(blank=True)
    project = models.ForeignKey(Project,
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True
                                )
    task = models.ForeignKey(Task,
                             on_delete=models.CASCADE,
                             blank=True,
                             null=True
                             )
    comment = models.ForeignKey(Comment,
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True
                                )
    message = models.ForeignKey(Message,
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True
                                )

    class Meta:
        verbose_name_plural = 'Calendar Events'

    @classmethod
    def get_events(cls):
        events = []
        for project in Project.objects.all():
            events.append(CalendarEvent(
                title=project.title,
                start_time=project.created_at,
                end_time=project.deadline,
                project=project
            ))
        for task in Task.objects.all():
            events.append(CalendarEvent(
                title=task.title,
                start_time=task.created_at,
                end_time=task.due_date,
                task=task
            ))
        for comment in Comment.objects.all():
            events.append(CalendarEvent(
                title=f'Comment on {comment.content_type}',
                start_time=comment.created_at,
                end_time=comment.created_at,
                comment=comment
            ))
        for message in Message.objects.all():
            events.append(CalendarEvent(
                title=message.title,
                start_time=message.created_at,
                end_time=message.created_at,
                message=message
            ))
        return events
