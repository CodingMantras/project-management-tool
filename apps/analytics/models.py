from django.db import models

from project.models import Project
from tasks.models import Task
from comments.models import Comment
from attachments.models import Attachment
from tags.models import Tag
from teams.models import Team
from users.models import CustomUser


class Analytics(models.Model):
    project_count = models.IntegerField(default=0)
    task_count = models.IntegerField(default=0)
    completed_task_count = models.IntegerField(default=0)
    overdue_task_count = models.IntegerField(default=0)
    avg_time_to_complete_task = models.DurationField(null=True, blank=True)
    comment_count = models.IntegerField(default=0)
    attachment_count = models.IntegerField(default=0)
    tag_count = models.IntegerField(default=0)
    team_count = models.IntegerField(default=0)
    user_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Analytics'

    @staticmethod
    def update_analytics():
        analytics, created = Analytics.objects.get_or_create(id=1)
        analytics.project_count = Project.objects.count()
        analytics.task_count = Task.objects.count()
        analytics.completed_task_count = Task.objects.filter(
            completed=True).count()
        analytics.overdue_task_count = Task.objects.filter(
            completed=False, due_date__lt=datetime.now().date()).count()
        analytics.comment_count = Comment.objects.count()
        analytics.attachment_count = Attachment.objects.count()
        analytics.tag_count = Tag.objects.count()
        analytics.team_count = Team.objects.count()
        analytics.user_count = CustomUser.objects.count()
        analytics.save()
