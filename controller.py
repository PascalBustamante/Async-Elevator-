import time
import asyncio
from enum import Enum
from turtle import up
#from elevator import Elevator

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
        d = Elevator.direction #should be 1 or -1 
        if Elevator.currentFloor < 6 and Elevator.currentFloor > -1:
            Elevator.currentFloor += d*1 
            return ("Elevator on floor " + Elevator.currentFloor) 
        else: #change direction
            Elevator.direction = -1*Elevator.direction
            return ("TEST HIT TOP OR BOTTOOM FLOORS")

    async def openCloseDoors(self, delay, Elevator):
        await asyncio.sleep(delay)
        return ("Elevator stopping at floor " + Elevator.currentFloor)

    async def checkCalls(self, upCalls, downCalls, inCalls, Elevator):
        d = self.Elevator.direction
        f = Elevator.currentFloor
        if d == 1:
            if upCalls[f] == 1:
                self.openCloseDoors(5,Elevator)
                upCalls[f] = 0
            elif inCalls[f] == 1:
                self.openCloseDoors(5,Elevator)
                inCalls[f] = 0
            else: return ("No stop requested on " + Elevator.currentFloor)
            if 1 in upCalls[f::] or 1 in inCalls[f::]:
                return 1
            elif 1 in upCalls[::f] or 1 in inCalls[::f]:
                Elevator.direction = -1
                return 1
            

        else:
            if downCalls[f] == 1:
                self.openCloseDoors(5,Elevator)
                downCalls[f] = 0
            elif inCalls[f] == 1:
                self.openCloseDoors(5,Elevator)
                inCalls[f] = 0
            else: print ("No stop requested on " + Elevator.currentFloor)
            if 1 in downCalls[f::] or 1 in inCalls[f::]:
                return 1
            elif 1 in downCalls[::f] or 1 in inCalls[::f]:
                Elevator.direction = 1
                return 1
        return 0  #meaning stop
        