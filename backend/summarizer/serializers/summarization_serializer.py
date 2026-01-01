# summarizer/serializers/summarization_serializer.py

from rest_framework import serializers

class SummarizationRequestSerializer(serializers.Serializer):
    text = serializers.CharField(
        min_length=20,
        max_length=6000,
        allow_blank=False,
        trim_whitespace=True
    )


class SummarizationResponseSerializer(serializers.Serializer):
    summary = serializers.CharField()
