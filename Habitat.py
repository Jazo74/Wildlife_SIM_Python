
import Animal
import ToolBox
import random
import AnimalNotExistException

#[Serializable]
class Habitat:
    # Base Properties
    HabitatName: str
    #[XmlIgnore]
    SumReqHeat: int
    #[XmlIgnore]
    SumReqOxigen: int
    #[XmlIgnore]
    SumReqWater: int
    #[XmlIgnore]
    SumReqFood: int
    #[XmlIgnore]
    SumReqEnergy: int
    AnimalList = [] # list of Animalobjects
    #[XmlIgnore]
    AnimalDict = {} # Dictionary<string, int>
    #Constructor
    def __init__(self, HabitatName):
        this.HabitatName = HabitatName
        SumReqHeat = 0
        SumReqOxigen = 0
        SumReqWater = 0
        SumReqFood = 0
        SumReqEnergy = 0

    def GatherAllReq(self):
        SumReqEnergy = 0
        SumReqFood = 0
        SumReqHeat = 0
        SumReqOxigen = 0
        SumReqWater = 0
        for member in AnimalList:
            SumReqHeat += member.ReqHeatUnit
            SumReqOxigen += member.ReqOxigenUnit
            SumReqFood += member.ReqFoodUnit
            SumReqWater += member.ReqWaterUnit
            SumReqEnergy += member.ReqEnergyUnit
    def SetHabitatName(self, habitatName):
        this.HabitatName = habitatName
    def SumAnimals(self):
        AnimalDict.Clear()
        for member in AnimalList:
            if AnimalDict.ContainsKey(member.SpeciesName) == False:
                AnimalDict.append(member.SpeciesName, 1)
            else:
                AnimalDict[member.SpeciesName] += 1 
    def AddNewAnimal(self, SpeciesName, Type, Environment):
        AnimalList.append(Animal(SpeciesName, Type, Environment))
    def RelocateAnimal(self, OwnName):
        found = False
        for index in range(len(AnimalList),0,-1):
            if AnimalList[index].OwnName == OwnName:
                AnimalList.RemoveAt(index)
                found = True
        if found == False:
            raise AnimalNotExistException()
    def Birth(self):
        if random.randint(0,100) > 90:
            if len(AnimalList) > 0:
                index = random.randint(0, len(AnimalList))
                ToolBox.WriteLineGreen("A " + AnimalList[index].SpeciesName + " baby has born!")
                AddNewAnimal(AnimalList[index].SpeciesName, AnimalList[index].Type, AnimalList[index].IdealEnvironment)
    def Dying(self):
        if random.randint(0, 100) > 98:
            if AnimalList.Count > 50:
                index = random.randint(0, len(AnimalList))
                ToolBox.WriteLineRed("A " + AnimalList[index].SpeciesName + " has died!")
                AnimalList.RemoveAt(index)