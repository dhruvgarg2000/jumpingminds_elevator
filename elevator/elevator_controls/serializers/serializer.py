from rest_framework import serializers


class ElevatorMovingStatusSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    moving_status = serializers.IntegerField(required=True)


class ElevatorNextDestinationSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    next_destination = serializers.SerializerMethodField()

    def get_next_destination(self, obj):
        if obj.service_request:
            return obj.service_request[0]
        return obj.current_floor


class ElevatorServiceRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    service_request = serializers.ListField(required=True)