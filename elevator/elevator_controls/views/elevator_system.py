from rest_framework.response import Response
from rest_framework import viewsets, status

from elevator_controls.models import Elevator

class ElevatorSystemViewSet(viewsets.ViewSet):

    def create(self,request):
        try:
            number_of_elevators = request.data.get("number_of_elevators", 0)
            if not number_of_elevators:
                return Response({"error" : "Please provide the number of elevators"}, status=status.HTTP_400_BAD_REQUEST)
            for _ in range(number_of_elevators):
                Elevator.objects.create()
            return Response(status=status.HTTP_201_CREATED)
        except:
            return Response({"error" : "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)