from django.db import models
from django.utils.text import slugify
from uuid import uuid4
from config.models import CreationModificationDateBase


class Project(CreationModificationDateBase):
    id = models.UUIDField(primary_key=True,
                          default=uuid4,
                          editable=False
                          )
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,
                            unique=True
                            )
    description = models.TextField()
    end_date = models.DateField(null=True,
                                blank=True
                                )
    created_by = models.ForeignKey("users.CustomUser",
                                   on_delete=models.CASCADE,
                                   related_name="projects_created"
                                   )
    STATUS_CHOICES = [
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
        ("on_hold", "On Hold")
    ]
    status = models.CharField(max_length=20,
                              choices=STATUS_CHOICES,
                              default="in_progress"
                              )
    is_active = models.BooleanField(default=True)
    teams = models.ManyToManyField('teams.Team',
                                   related_name='projects'
                                   )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_tasks(self):
        return self.tasks.all()
