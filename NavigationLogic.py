import time
import asyncio
from enum import Enum
from elevator import Elevator
from controller import Navigator


q = asyncio.Queue()
elevator1 = Elevator()
controller = Navigator() 
while True:
    userInput = asyncio.ensure_future(input("enter a floor and direction as a tuple")) #they'll come in as lists (floor, [up=1, down=-1, in=0])
    q.put(userInput)

    while q.empty() != False:
        r = q.get()
        if r[2] == 1:
            Navigator.upCalls[r[1]] = 1
        elif r[2] == -1:
            Navigator.downCalls[r[1]] = 1
        else:
            Navigator.inCalls[r[1]] =1
    out = Navigator.checkCalls(Navigator.upCalls, Navigator.downCalls, Navigator.inCalls)
    if out == 1:
        Navigator.movementBetweenFloors(5,elevator1)

















