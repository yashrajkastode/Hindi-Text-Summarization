from django.urls import path
from summarizer.views import SummarizeAPIView, TaskStatusAPIView

urlpatterns = [
    path("summarize/", SummarizeAPIView.as_view()),
    path("status/<uuid:task_id>/", TaskStatusAPIView.as_view()),
]
