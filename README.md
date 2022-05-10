# Async Elevator

# Classes:

## Event Classes
They are there to seperate the inputs coming in from the button methods in the Elevator class.
## Elevator 

It initializes the elevator controller class and has all the "public" methods attached to it. 

## ElevatorController

Has all the logic and "private" methods. Contains 3 lists outside_down, inside and outside_up with 6 indexes each to simulate the floors and the buttons. A 0 in these lists imply no call has been made while a 1 tells the elevator it needs to service that floor.

# Methods:

## Elevator Methods:

The inputs from the elevator class are passed to the ElevatorControll class via the button methods. These take the inputs, create their corresponding events and places them into the queue. 

## ElevatorControll Methods:

###### The 3 button methods (up_button, down_button and inside_button)
They place the inputs coming in from the button methods in the Elevator class and places them into the queue.

###### should_stop 
Checks to see if there has been a call in the floor the elevator is on, it also takes into account the direction of the elevator when stopping for outside calls.

###### move_up and move_down 
Move up or down the elevator as well as simulate the elevator movement by waiting for 5 seconds.

###### has_action 
Checks if there are any calls that the elevator needs to service. It is used in the run method to start a loop.

###### run 
First checks the has_action method to see if it needs to start the elevator. Then checks to see the direction of the elevator, then if it needs to service the floor it is currently in (if it does this is where the 5 seconds of wait to service the floor are simulated). Then checks if there any calls in the direction of the elevator. If there are any it moves towards them, if not it changes direction.

###### input_loop
Checks for calls continiously (via the queue_task below). Takes the inputs from the queue and assigns them to their corresponding lists. Finally it also creats a task for the run method above.

###### queue_task 
Creates a task for 


