import sys
import ResourcePool
import ConsoleSimulation
import UI

class Main:
    arkOne = ResourcePool

    def __init__(self):
        arkOne = ResourcePool("new")

    def __main__(self,args):
        arkOne = ResourcePool("new")
        p = Main()
        cSim = ConsoleSimulation()
        ui = UI(cSim)
        ui.Start(p)
