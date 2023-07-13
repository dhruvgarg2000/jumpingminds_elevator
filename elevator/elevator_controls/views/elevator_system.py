from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action
from elevator_controls.helpers.elevator_request_handler import (
    add_elevator_service_request,
    process_elevator
)
from elevator_controls.serializers.serializer import (
    ElevatorMovingStatusSerializer,
    ElevatorNextDestinationSerializer,
    ElevatorOperationalStatusSerializer,
    ElevatorSerializer,
    ElevatorServiceRequestSerializer,
)
from elevator_controls.models import Elevator

class ElevatorSystemViewSet(viewsets.ViewSet):

    def create(self,request):
        try:
            number_of_elevators = request.data.get("number_of_elevators", 0)
            # create n number of elevators
            if not number_of_elevators:
                return Response({"error" : "Please provide the number of elevators"}, status=status.HTTP_400_BAD_REQUEST)
            for _ in range(number_of_elevators):
                Elevator.objects.create()
            return Response(status=status.HTTP_201_CREATED)
        except:
            return Response({"error" : "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['post'])
    def elevator_request(self, request):
        try:
            target_floors = request.data.get('target_floors', [])
            # assign and add elevator service request to responsible elevator
            for target_floor in target_floors:
                add_elevator_service_request(target_floor)
            # run/process the elevator to execute the service request
            process_elevator()
            return Response(status=status.HTTP_201_CREATED)
        except:
            return Response({"error" : "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=["get"])
    def service_request(self, request):
        try:
            elevator_id = request.GET.get("elevator_id")
            elevator = Elevator.objects.get(id=elevator_id)
            serializer = ElevatorServiceRequestSerializer(elevator)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Elevator.DoesNotExist:
            return Response(
                {"error": "Elevator not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except:
            return Response(
                {"error": "Internal Server Error"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    @action(detail=False, methods=["get"])
    def next_destination(self, request):
        try:
            elevator_id = request.GET.get("elevator_id")
            elevator = Elevator.objects.get(id=elevator_id)
            serializer = ElevatorNextDestinationSerializer(elevator)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Elevator.DoesNotExist:
            return Response(
                {"error": "Elevator not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except:
            return Response(
                {"error": "Internal Server Error"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    @action(detail=False, methods=["get"])
    def moving_status(self, request):
        try:
            elevator_id = request.GET.get("elevator_id")
            elevator = Elevator.objects.get(id=elevator_id)
            serializer = ElevatorMovingStatusSerializer(elevator)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(
                {"error": "Internal Server Error"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    @action(detail=False, methods=["patch"])
    def update_operational_status(self, request):
        try:
            serializer = ElevatorOperationalStatusSerializer(data=request.data)
            if serializer.is_valid():
                elevator = Elevator.objects.get(id=serializer.data["id"])
                elevator.is_operational = serializer.data["is_operational"]
                elevator.save()
                serializer = ElevatorSerializer(elevator)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(
                    {"error": "Elevator ID and operational status are mandatory"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except:
            return Response(
                {"error": "Internal Server Error"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
