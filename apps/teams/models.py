from django.urls import reverse
from django.db import models

from tasks.models import Task
from config.models import CreationModificationDateBase


class Team(CreationModificationDateBase):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField('users.CustomUser', related_name='teams')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('team_detail', args=[str(self.id)])

    def get_members(self):
        return self.members.all()

    def add_member(self, user):
        if user not in self.members.all():
            self.members.add(user)
            self.save()

    def add_member(self, user, role='member', permissions=None):
        member = TeamMember(team=self, user=user, role=role,
                            permissions=permissions)
        member.save()

    def remove_member(self, user):
        if user in self.members.all():
            self.members.remove(user)
            self.save()

    def is_member(self, user):
        return user in self.members.all()

    def get_active_members(self):
        return self.members.filter(is_active=True)

    def get_inactive_members(self):
        return self.members.filter(is_active=False)

    def set_active(self):
        self.is_active = True
        self.save()

    def set_inactive(self):
        self.is_active = False
        self.save()

    def get_assigned_tasks(self):
        return Task.objects.filter(assigned_to__in=self.members.all())


class TeamMember(models.Model):
    TEAM_ROLES = [
        ('leader', 'Team Leader'),
        ('manager', 'Project Manager'),
        ('member', 'Team Member'),
    ]

    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    role = models.CharField(choices=TEAM_ROLES,
                            default='member',
                            max_length=20
                            )
    permissions = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.email} ({self.role})"


class Attachment(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    file = models.FileField(upload_to='attachments')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description
