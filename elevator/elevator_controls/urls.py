from django.urls import path, include
from rest_framework import routers
from elevator_controls.views.initialize_elevator_system import ElevatorSystemViewSet

router = routers.DefaultRouter()

router.register('', ElevatorSystemViewSet, basename="elevator")

urlpatterns = [
    path('api/', include(router.urls)),
]