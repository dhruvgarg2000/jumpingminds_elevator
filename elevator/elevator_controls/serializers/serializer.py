from rest_framework import serializers


class ElevatorServiceRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    service_request = serializers.ListField(required=True)