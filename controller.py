import time
import queue
import asyncio
from enum import Enum
from elevator import Elevator

class Navigator(object):
    def __init__(self, floors, Elevator):
        self.floors = floors
        self.elevator = Elevator
        self.upCalls = list()
        self.downCalls = list()
        self.inCalls = list()
        for x in range(floors):
            self.upCalls.append(0)
            self.downCalls.append(0)
            self.inCalls.append(0)


    async def movementBetweenFloors(delay, Elevator):
        await asyncio.sleep(delay)
        d = Elevator.direction #should be 1,0 or -1 (NEED to get rid of the 0)
        if Elevator.currentFloor < 6 and Elevator.currentFloor > -1:
            if d != 0: #not needed with new idea
                Elevator.currentFloor += d*1 
                print ("Elevator on floor " + Elevator.currentFloor) #I think i need to be returning instead
        else: #change direction
            Elevator.direction = -1*Elevator.direction
            print("TEST HIT TOP OR BOTTOOM FLOORS")

    async def openCloseDoors(delay, Elevator):
        await asyncio.sleep(delay)
        print ("Elevator stopping at floor " + Elevator.currentFloor)

    async def checkCalls(upCalls, downCalls, inCalls, Elevator):
        d = Elevator.direction`
        f = Elevator.currentFloor`
        if d == 1:
            if upCalls[f] == 1:
                openCloseDoors(5,Elevator)
                upCalls[f] = 0
            elif inCalls[f] == 1:
                openCloseDoors(5,Elevator)
                inCalls[f] = 0
            else: print ("No stop requested on " + Elevator.currentFloor)
        else:
            if downCalls[f] == 1:
                openCloseDoors(5,Elevator)
                downCalls[f] = 0
            elif inCalls[f] == 1:
                openCloseDoors(5,Elevator)
                inCalls[f] = 0
            else: print ("No stop requested on " + Elevator.currentFloor)