from django.db import models

# Create your models here.
class Elevator(models.Model):
    class Meta:
        db_table = 'elevators'

    class ElevatorMovingStatusChoices(models.TextChoices):
        NOT_MOVING = 0, "Not Moving"
        UP = 1, "Moving Upward"
        DOWN = -1, "Moving Downward"

    id = models.AutoField(primary_key=True)
    moving_status = models.IntegerField(choices=ElevatorMovingStatusChoices.choices, default=ElevatorMovingStatusChoices.NOT_MOVING)
    is_door_open = models.BooleanField(default=False, null=False)
    is_operational = models.BooleanField(default=True, null=False)
    current_floor = models.IntegerField(default=0)
    target_floor = models.IntegerField(default=0)
    service_request = models.JSONField(default=list)