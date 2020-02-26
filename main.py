class Main:
    public ResourcePool arkOne

    def __init__(self):
        arkOne = ResourcePool("new")

    def __main__(self,args):
        p = Main()
        cSim = ConsoleSimulation()
        ui = UI(cSim)
        ui.Start(p)
