from django.urls import path, include
from . import views

app_name = 'administrator'

urlpatterns = [
    path('',
         views.AdmindashboardTemplateView.as_view(),
         name="admin_dashboard_url"
         )
]
