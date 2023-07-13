import time
from elevator_controls.models import Elevator


def add_elevator_service_request(target_floor):
    minimum_difference = 1000
    selected_elevator = ''
    elevator_objs = Elevator.objects.all()
    # find the closest elevator
    for elevator_obj in elevator_objs:
        if elevator_obj.is_operational:
            if elevator_obj.service_request:
                position = elevator_obj.service_request[-1]
            else:
                position = elevator_obj.current_floor
            if abs(target_floor - position) < minimum_difference:
                minimum_difference = abs(target_floor - position)
                selected_elevator = elevator_obj
    selected_elevator.service_request.append(target_floor)
    selected_elevator.save()
    return

def process_elevator():
    elevator_objs = Elevator.objects.all()
    # move the elevator to the target floor
    for elevator in elevator_objs:
        for _ in range(len(elevator.service_request)):
            target_floor = elevator.service_request[0]
            print("Target Floor:", target_floor)
            elevator.target_floor = target_floor
            elevator.moving_status = elevator_moving_direction(elevator, target_floor)
            elevator.save()
            time.sleep(abs(elevator.target_floor - elevator.current_floor))
            elevator.is_door_open = True
            elevator.save()
            print("Door is opening")
            time.sleep(5)
            elevator.is_door_open = False
            elevator.current_floor = target_floor
            elevator.service_request.remove(target_floor)
            elevator.save()
        elevator.moving_status = 0
        elevator.save()

def elevator_moving_direction(elevator, target_floor):
    if elevator.current_floor < target_floor:
        return 1
    elif elevator.current_floor > target_floor:
        return -1
    return 0