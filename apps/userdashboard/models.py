from django.db import models
from django.conf import settings


class UserPreference(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    theme = models.CharField(max_length=50)
    language = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user}'s Preferences"


class SavedSearch(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    search_query = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}'s Saved Search: {self.search_query}"
