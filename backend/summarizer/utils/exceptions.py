# summarizer/utils/exceptions.py

from rest_framework.exceptions import APIException
from rest_framework import status


class SummarizationError(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = "Text summarization failed."
    default_code = "summarization_error"


class ModelNotLoadedError(APIException):
    status_code = status.HTTP_503_SERVICE_UNAVAILABLE
    default_detail = "Summarization model is not available."
    default_code = "model_unavailable"
