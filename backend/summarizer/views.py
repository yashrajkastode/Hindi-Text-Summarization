from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from celery.result import AsyncResult

from summarizer.serializers.summarization_serializer import (
    SummarizationRequestSerializer,
)
from summarizer.tasks import summarize_text_task


class SummarizeAPIView(APIView):
    """
    POST /api/summarize/
    Body: { "text": "<hindi text>" }

    Returns:
    { "task_id": "<uuid>" }
    """

    def post(self, request):
        serializer = SummarizationRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        task = summarize_text_task.delay(
            serializer.validated_data["text"]
        )

        return Response(
            {"task_id": task.id},
            status=status.HTTP_202_ACCEPTED,
        )


class TaskStatusAPIView(APIView):
    """
    GET /api/status/<task_id>/

    Returns:
    - PENDING
    - STARTED
    - SUCCESS + summary
    """

    def get(self, request, task_id):
        result = AsyncResult(task_id)

        if result.successful():
            return Response(
                {
                    "status": "SUCCESS",
                    "summary": result.result,
                },
                status=status.HTTP_200_OK,
            )

        return Response(
            {"status": result.status},
            status=status.HTTP_200_OK,
        )
