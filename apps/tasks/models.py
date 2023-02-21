from django.db import models
from config.models import CreationModificationDateBase


class Task(CreationModificationDateBase):
    project = models.ForeignKey("project.Project",
                                on_delete=models.CASCADE,
                                related_name="tasks")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True,
                                   null=True
                                   )
    due_date = models.DateField()
    completed = models.BooleanField(default=False)
    assigned_to = models.ForeignKey("users.Customuser",
                                    on_delete=models.CASCADE,
                                    related_name="tasks")
    priority = models.CharField(max_length=20,
                                choices=(
                                    ('HIGH', 'High'),
                                    ('MEDIUM', 'Medium'),
                                    ('LOW', 'Low')
                                ))
    tags = models.ManyToManyField("Tag",
                                  blank=True
                                  )
    comments = models.ManyToManyField("Comment",
                                      blank=True
                                      )
    attachments = models.ManyToManyField("Attachment",
                                         blank=True
                                         )
    subtasks = models.ManyToManyField("Subtask",
                                      blank=True
                                      )
    team = models.ForeignKey("teams.Team",
                             on_delete=models.CASCADE,
                             related_name='tasks',
                             null=True
                             )

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.TextField()
    created_by = models.ForeignKey("users.Customuser",
                                   on_delete=models.CASCADE,
                                   related_name="comments"
                                   )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text[:20]}..."


class Attachment(models.Model):
    file = models.FileField(upload_to="attachments/")
    uploaded_by = models.ForeignKey("users.Customuser",
                                    on_delete=models.CASCADE,
                                    related_name="attachments"
                                    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name


class Subtask(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
