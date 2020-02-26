import Habitat
import HeatCollector
import FoodReplicator
import OxigenGenerator
import SolarPanel
import WaterFilter

class ResourcePool:
    habitatList = []
    HeatCollectors = []
    SolarPanels = []
    OxigenGenerators = []
    FoodReplicators = []
    WaterFilters = []

    AllHeatReq: int = 0
    AllEnergyReq: int = 0
    AllOxigenReq: int = 0
    AllFoodReq: int = 0
    AllWaterReq: int = 0

    AllHeatCapacity: int = 0
    AllEnergyCapacity: int = 0
    AllOxigenCapacity: int = 0
    AllFoodCapacity: int = 0
    AllWaterCapacity: int = 0

    HeatLoad: float = 0.0
    EnergyLoad: float = 0.0
    OxigenLoad: float = 0.0
    FoodLoad: float = 0.0
    WaterLoad: float = 0.0

    def __init__(self, State): #constructor
        if State == "new":
            habitatList.append(Habitat("Rainforest"))
            habitatList.append(Habitat("Temperate Forest"))
            habitatList.append(Habitat("Sea"))
            habitatList.append(Habitat("Arctic"))
            habitatList.append(Habitat("Savannah"))
            HeatCollectors.append(HeatCollector()
            SolarPanels.append(SolarPanel())
            FoodReplicators.append(FoodReplicator())
            OxigenGenerators.append(OxigenGenerator())
            WaterFilters.append(WaterFilter())
    def ResourceCycle(self): # Resource math
        SumAllRequiredResource()
        SumAllCapacity()
        CheckBalance()
        SetLoad()
    def SumAllRequiredResource(self): # gather all the required resources
        AllHeatReq = 0
        AllEnergyReq = 0
        AllFoodReq = 0
        AllOxigenReq = 0
        AllWaterReq = 0
        for habitat in habitatList:
            habitat.GatherAllReq()
            AllHeatReq += habitat.SumReqHeat
            AllEnergyReq += habitat.SumReqEnergy
            AllFoodReq += habitat.SumReqFood
            AllOxigenReq += habitat.SumReqOxigen
            AllWaterReq += habitat.SumReqWater
    def SumAllCapacity(self): # Sum all the current capacity of the facilities
        AllHeatCapacity = 0
        AllEnergyCapacity = 0
        AllFoodCapacity = 0
        AllOxigenCapacity = 0
        AllWaterCapacity = 0
        for heatCollector in HeatCollectors:
            AllHeatCapacity += heatCollector.Capacity
        for solarPanel in SolarPanels:
            AllEnergyCapacity += solarPanel.Capacity
        for foodReplicator in FoodReplicators:
            AllFoodCapacity += foodReplicator.Capacity
        for oxigenGenerator in OxigenGenerators:
            AllOxigenCapacity += oxigenGenerator.Capacity
        for waterFilter in WaterFilters:
            AllWaterCapacity += waterFilter.Capacity
    def CheckBalance(self): #Checking the input/output balance
        while AllHeatReq > AllHeatCapacity:
            HeatCollectors.append(HeatCollector())
            SumAllCapacity()
        while AllEnergyReq > AllEnergyCapacity:
            SolarPanels.append(SolarPanel())
            SumAllCapacity()
        while AllFoodReq > AllFoodCapacity:
            FoodReplicators.append(FoodReplicator())
            SumAllCapacity()
        while AllOxigenReq > AllOxigenCapacity:
            OxigenGenerators.append(OxigenGenerator())
            SumAllCapacity()
        while AllWaterReq > AllWaterCapacity:
            WaterFilters.append(WaterFilter())
            SumAllCapacity()
    def SetLoad(self): # Set the neccessary loads
        HeatLoad = Math.Round(AllHeatReq / (decimal)AllHeatCapacity * 100, 0)
        EnergyLoad = Math.Round(AllEnergyReq / (decimal)AllEnergyCapacity * 100, 0)
        FoodLoad = Math.Round(AllFoodReq / (decimal)AllFoodCapacity * 100, 0)
        OxigenLoad = Math.Round(AllOxigenReq / (decimal)AllOxigenCapacity * 100, 0)
        WaterLoad = Math.Round(AllWaterReq / (decimal)AllWaterCapacity * 100, 0)
    def CreatingAHabitat(self, habitatName): # Creating a new habitat
        NewHabitat = Habitat(habitatName)
        habitatList.Add(NewHabitat)
    def RemovingAHabitat(self, habitatName): # Removing a new habitat
        if not IsHabitatExist(habitatName):
            throw new HabitatNotExistException()
        for (int index = habitatList.Count-1; index >= 0; index--)
            if habitatList[index].HabitatName == habitatName:
                if habitatList[index].AnimalList.Count > 0:
                    throw new NotEmptyHabitatException()
                habitatList.RemoveAt(index)
    def GetHabitats(self): # Get the list of all habitats
        return habitatList
    def IsHabitatExist(sself, habitatName): # Checking if the habitat exist
        for habitat in habitatList:
            if habitat.HabitatName == habitatName:
                return true
        return false
    def AddNewAnimal(self, SpeciesName, Type, Environment): # Adding new animals 
        if  not IsHabitatExist(Environment):
            throw new HabitatNotExistException()
        for habitat in habitatList:
            if habitat.HabitatName == Environment:
                habitat.AddNewAnimal(SpeciesName, Type, Environment)
    def FindAnimal(self, OwnName): # Checking if an animal exist in the system
        for habitat in habitatList:
            for animal in habitat.AnimalList:
                if animal.OwnName == OwnName:
                    return animal
        throw new AnimalNotExistException()
    def RelocateAnimal(self, OwnName): # Relocating (removing) an animal from the system
        for habitat in habitatList:
            habitat.RelocateAnimal(OwnName)
    def BirthDay(self): # Reproduction function
        for habitat in habitatList:
            habitat.Birth()
    def Dying(self): # 
        for habitat in habitatList:
            habitat.Dying()
    def SerializeMyList(self): # serializing the data to an xml file
        XmlSerializer xmlBuild = new XmlSerializer(habitatList.GetType())
        FileStream file = new FileStream("sanctuary.xml", FileMode.Create)
        xmlBuild.Serialize(file, habitatList)
        file.Close()
    def DeSerializeMyList(self): # deserializing the the date from an xml file
        if  not File.Exists("sanctuary.xml"):
            throw new FileNotExistException()
        XmlSerializer xmlBuild = new XmlSerializer(habitatList.GetType())
        FileStream file = new FileStream("sanctuary.xml", FileMode.Open)
        habitatList.Clear()
        List<Habitat> newObject = (List<Habitat>)xmlBuild.Deserialize(file)
        habitatList = newObject
        file.Close()
