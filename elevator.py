class Elevator(object):
    def __init__(self):
        self.currentFloor = 0
        self.direction = 1 #1 = up, -1 = down (maybe i can get tid of 0 and only keep the old direction)
        self.destination = 0 
