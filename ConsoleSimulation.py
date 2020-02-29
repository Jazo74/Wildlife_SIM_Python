import os
import ToolBox
class ConsoleSimulation:
    # Running the simulation
    def LifeCycle(self, p, cycleTime): 
        while not readchar. Console.KeyAvailable:
            os.system("Clear")
            p.arkOne.ResourceCycle()
            ShowAnimals(p)
            ShowRequiredResources(p)
            ShowResourceGenerators(p)
            p.arkOne.BirthDay()
            p.arkOne.Dying()
            Thread.Sleep(cycleTime)
    # Showing the informations of the population by zones
    def ShowAnimals(self, p):
        ToolBox.WriteLineBlue("----------------------------------------------------------------------------------------------")
        ToolBox.WriteLineBlue("Current Population:")
        for habs in p.arkOne.GetHabitats():
            habs.SumAnimals()
            print(habs.HabitatName.PadRight(18))
            for KeyValuePair<string, int> x in habs.AnimalDict:
                tempString: str = x.Key.PadRight(11) + " " + x.Value
                print(tempString.PadRight(17))
            print()
    #Showing the required resources by zones
    def ShowRequiredResources(self, p): 
        ToolBox.WriteLineBlue("---------------------------------------------------------------------------------------------")
        ToolBox.WriteLineBlue("Required Resources:")
        ToolBox.WriteLineBlue("Zone                  Energy(kW)   Heat(kJ)   Food(unit)   Water(m3)   Oxigen(m3)")
        for member in p.arkOne.GetHabitats():
            print(member.HabitatName.ToString().PadRight(19))
            print(member.SumReqEnergy.ToString().PadLeft(9))
            print(member.SumReqHeat.ToString().PadLeft(11))
            print(member.SumReqFood.ToString().PadLeft(11))
            print(member.SumReqWater.ToString().PadLeft(14))
            print(member.SumReqOxigen.ToString().PadLeft(13))
    # Showing the current state of the supporting facilities
    def ShowResourceGenerators(self, p): 
        ToolBox.WriteLineBlue("---------------------------------------------------------------------------------------------")
        ToolBox.WriteLineBlue("Running Facilities:")
        print("Heatcollectors".PadRight(19) + p.arkOne.HeatCollectors.Count + " block, Load: " + p.arkOne.HeatLoad + " %")
        print("Solarpanels".PadRight(19) + p.arkOne.SolarPanels.Count + " block, Load: " + p.arkOne.EnergyLoad + " %")
        print("Foodreplicators".PadRight(19) + p.arkOne.FoodReplicators.Count + " block, Load: " + p.arkOne.FoodLoad + " %")
        print("Oxigen generators".PadRight(19) + p.arkOne.OxigenGenerators.Count + " block, Load: " + p.arkOne.OxigenLoad + " %")
        print("Water filters: ".PadRight(19) + p.arkOne.WaterFilters.Count + " block, Load: " + p.arkOne.WaterLoad + " %")
        ToolBox.WriteLineBlue("---------------------------------------------------------------------------------------------")
        ToolBox.WriteLineBlue("Messages:")
