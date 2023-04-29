from django.urls import path
from app.views.HomeView import HomeView
from app.views.ApiView import ApiView
from app.views.SubjectView import SubjectView


urlpatterns = [
    path("", HomeView.as_view(), name="home"),

    path("get-api", ApiView.as_view(), name="get-api"),
    path("post-api", ApiView.get, name="post-api"),
    path("get-subjects", SubjectView.as_view(), name="get-subjects"),
    path("post-subject/<int:value>", SubjectView.post, name="post-subject"),
]