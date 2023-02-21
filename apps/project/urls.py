from django.urls import path
from . import views

app_name = 'project'

urlpatterns = [
    path("create/",
         views.ProjectCreateView.as_view(),
         name="create_project_url"
         ),
    path("list/",
         views.ProjectListView.as_view(),
         name="project_list_url"
         ),
    path("detail/<int:pk>/",
         views.ProjectDetailView.as_view(),
         name="project_detail_url"
         ),
    path("update/<int:pk>/",
         views.ProjectUpdateView.as_view(),
         name="project_update_url"
         ),
    path("delete/<int:pk>/",
         views.ProjectDeleteView.as_view(),
         name="project_delete_url"
         ),
]
