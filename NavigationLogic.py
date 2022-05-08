import time
import queue
import asyncio
from enum import Enum

class direction(Enum):
    up = 1
    stationary = 0
    down = -1

class elevator(object):
    def __init__(self) -> None:
        self.currentFloor = 0
        self.towards = 0
    

class Controller(object):
    floors = 5 #including 0

q = queue.Queue()
#add inputs into queue
#might need 2 queues to seperate the outside and inside calls

while q.empty() == False: #not sure if this even works or is needed (the != bit)
    f = q.get() #should be an int 0-5 
    async def elevatorMovement(delay, queue): #if we put the queue here we must add the loop that fills the calls in the list, the other way would be to have it outside and just put floor
        #first check direction
        #check 1s in the direction first
        #if going up
        #most of what is happening below we can place it as a method 
        if direction == 1: #not right
            while 1 in calls:
                if elevatorFloor != 5:
                    elevatorFloor += 1
                    calls[elevatorFloor] = 0
                else: #change direction to 0 or -1
                    test = 1 
                while queue.empty() == False:
                    f = queue.get()
                    calls[f] = 1
        if direction == -1: #not right
            while 1 in calls:
                if elevatorFloor != 0:
                    elevatorFloor -= 1
                    calls[elevatorFloor] = 0
                else: #change direction to 0 or -1
                    test = 1 
                while queue.empty() == False:
                    f = queue.get()
                    if f != elevatorFloor:
                        calls[f] = 1
        


elevatorFloor = 0
elevatorDirection = 0
calls = [0,0,0,0,0,0]
#outSideCalls = [0,0,0,0,0,0]
#inSideCalls = [0,0,0,0,0,0]

