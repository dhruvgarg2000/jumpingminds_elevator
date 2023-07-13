from django.urls import path, include
from rest_framework import routers
from elevator_controls.views.elevator_system import ElevatorSystemViewSet

router = routers.SimpleRouter()

router.register('', ElevatorSystemViewSet, basename="elevator")

urlpatterns = [
    path('api/', include(router.urls)),
]