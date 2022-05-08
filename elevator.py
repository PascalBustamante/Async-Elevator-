import time
import queue
import asyncio
from enum import Enum

from NavigationLogic import direction

q = queue.Queue()

class Elevator(object):
    def __init__(self):
        self.currentFloor = 0
        self.direction = 0 #0 = stationary, 1 = up, -1 = down (maybe i can get tid of 0 and only keep the old direction)
        self.destination = 0 

    #set destination
    f = q.get(False)
    self.destination 