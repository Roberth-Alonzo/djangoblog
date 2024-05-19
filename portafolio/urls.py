from django.urls import path
from .views import project_detail

app_name= 'VideoGame'

urlpatterns =[
    path("<int:project_id>", project_detail, name="project_detail")
]