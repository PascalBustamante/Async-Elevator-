import asyncio
from elevator import Elevator


class Simulation(object):
    async def simple_simulation(self): 
        elevator = Elevator() 
        print(elevator.get_current_floor())
        await elevator.run() #start the elevator
        print(elevator.get_current_floor())
        await elevator.inside_button(2)
        print("2 but pressed")
        await asyncio.sleep(10)
        print(elevator.get_current_floor())
        print(elevator._controller._inside)

        await asyncio.sleep(5)
        print(elevator.get_current_floor())
        
        print("4but")
        await elevator.inside_button(3)
        print(elevator._controller._inside)
        print(elevator.get_current_floor())
        await elevator.down_button(4)
        await elevator.inside_button(5)
        await elevator.up_button(2)
        await elevator.down_button(2)
        await elevator.inside_button(1)
        await elevator.inside_button(6)
        await asyncio.sleep(10)
        print(elevator.get_current_floor())

        await asyncio.sleep(10)
        print(elevator.get_current_floor())

        await asyncio.sleep(10)
        print(elevator.get_current_floor())
        await elevator.inside_button(3)
        await asyncio.sleep(10)
        await elevator.inside_button(5)
        print(elevator._controller._inside)
        await asyncio.sleep(10)
        print(elevator.get_current_floor())
        await asyncio.sleep(10)
        print(elevator.get_current_floor())
        await asyncio.sleep(10)
        print(elevator.get_current_floor())
        await asyncio.sleep(10)
        print(elevator.get_current_floor())
        await asyncio.sleep(10)
        print(elevator.get_current_floor())
        await asyncio.sleep(10)
    
   


async def main():
    sim = Simulation()
    
    print ("Running Simulation X")
    await sim.simple_simulation()

asyncio.run(main())



#the run loop is not being triggered because we are not in the input_loop 
#maybe we need to intialize it in main? 