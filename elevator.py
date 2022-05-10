import asyncio
from enum import Enum

class Direction(Enum): #Keeps track of the direction of the elevator
    UP = 1
    DOWN = 2


class UpEvent(object):
    def __init__(self, floor):
        self.input_floor = floor

class DownEvent(object):
    def __init__(self, floor):
        self.input_floor = floor

class InsideEvent(object):
    def __init__(self, floor):
        self.input_floor = floor

class ElevatorController:
    def __init__(self):
        self._floor = 0
        self._direction = Direction.UP
        self._queue = asyncio.Queue()
        self._inside = [0,0,0,0,0,0]
        self._outside_up = [0,0,0,0,0,0]
        self._outside_down = [0,0,0,0,0,0]
        self._run_task = None
        self._event_task = None

    async def up_button(self, input_floor): #take button inputs, assign it to their coresponding class and add it to a queue  
        await self._queue.put(UpEvent(input_floor))

    async def down_button(self, input_floor):
        await self._queue.put(DownEvent(input_floor))

    async def inside_button(self, input_floor):
        await self._queue.put(InsideEvent(input_floor))
    
    async def should_stop(self, floor): #checks if the elevator needs to stop or not
        if self._inside[floor] == 1: 
            self._inside[floor] = 0
            return True #returns true when a stop is requiered 
        elif self._direction is Direction.UP and self._outside_up[floor] == 1: #makes sure the elevator is going the direction that the call from outside made
            self._outside_up[floor] = 0
            return True
        elif self._direction is Direction.DOWN and self._outside_down[floor] == 1:
            self._outside_down[floor] = 0
            return True
        else:
            return False #returns false when a stop is not

    async def move_up(self): #moves up the elevator by 1
        await asyncio.sleep(5) #waits 5 secs to simulate the elevator moving between floors
        if self._floor < 6: #makes sure we are not already on the highest floor
            self._floor +=1

    async def move_down(self): #moves down the elevator by 1
        await asyncio.sleep(5) #waits 5 secs to simulate the elevator moving between floors
        if self._floor > 0: #makes sure we are not already on the lowest floor
            self._floor -=1

    def has_actions(self): #checks if we need to move the elevator at all
        if 1 in self._inside or 1 in self._outside_down or 1 in self._outside_up:
            return True
        else:
            return False #we keep the elevator stationary 

    async def run(self): #runs the main logic for the elevator
        while self.has_actions():
            if self._direction is Direction.UP:
                if 1 in self._inside[self._floor::] or 1 in self._outside_up[self._floor::]: #checks if there are more calls in direction
                    r = await self.should_stop(self._floor)
                    if r == True:
                        await asyncio.sleep(5) #waits 5 secs to simulate a stop
                        if self._floor < 5:
                            if 1 in self._inside[self._floor+1::] or 1 in self._outside_up[self._floor+1::]:
                                await self.move_up()
                    else:
                        await self.move_up()      
                else:
                    self._direction = Direction.DOWN #if no calls above change direction
            elif self._direction is Direction.DOWN:
                if 1 in self._inside[0:self._floor+1] or 1 in self._outside_down[0:self._floor+1]: #checks if there are more calls in direction
                    r = await self.should_stop(self._floor)
                    if r == True:
                        await asyncio.sleep(5) #waits 5 secs to simulate a stop
                        if self._floor > -1:
                            if 1 in self._inside[0:self._floor+1] or 1 in self._outside_down[0:self._floor+1]: 
                                await self.move_down()
                    else:
                        await self.move_down()
                else:
                    self._direction =Direction.UP #if no calls below change direction                                                                             


    async def queue_task(self): #creates a task to run the input_loop
        if self._event_task is None or self._event_task.done(): #makes sure we need to create a new task before making a new one
            self._event_task = asyncio.create_task(self.input_loop())


    async def input_loop(self): #processes the queue placing inputs into their corresponding event classes
        while True:
            self._event_task = await self._queue.get() #take items from the queue
            if isinstance(self._event_task, UpEvent):
                self._outside_up[self._event_task.input_floor-1] = 1
            elif isinstance(self._event_task, DownEvent):
                self._outside_down[self._event_task.input_floor-1] = 1
            elif isinstance(self._event_task, InsideEvent):
                self._inside[self._event_task.input_floor-1] = 1
            if self._run_task is None or self._run_task.done():#makes sure we need to create a new task before making a new one
                self._run_task = asyncio.create_task(self.run()) #creates a task to run the input_loop

class Elevator(object): #these are the " public" methods (just convention in python)
    def __init__(self):
        self._controller = ElevatorController()

    async def up_button(self, input_floor):
        await self._controller.up_button(input_floor)

    async def down_button(self, input_floor):
        await self._controller.down_button(input_floor)

    async def inside_button(self, input_floor):
        await self._controller.inside_button(input_floor)

    def get_current_floor(self):
        return self._controller._floor

    async def run(self): #runs the elevator
        await self._controller.queue_task()
