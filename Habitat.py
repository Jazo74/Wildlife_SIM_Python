
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
        foreach (Animal member in AnimalList)
            SumReqHeat += member.ReqHeatUnit
            SumReqOxigen += member.ReqOxigenUnit
            SumReqFood += member.ReqFoodUnit
            SumReqWater += member.ReqWaterUnit
            SumReqEnergy += member.ReqEnergyUnit
    def SetHabitatName(self, habitatName):
        this.HabitatName = habitatName
    def SumAnimals(self):
        AnimalDict.Clear()
        foreach (Animal member in AnimalList)
            if (AnimalDict.ContainsKey(member.SpeciesName) == false)
                AnimalDict.Add(member.SpeciesName, 1)
            else
                AnimalDict[member.SpeciesName] += 1 
    def AddNewAnimal(self, SpeciesName, Type, Environment):
        AnimalList.Add(new Animal(SpeciesName, Type, Environment));
    def RelocateAnimal(self, OwnName):
        bool found = false
        for (int index = AnimalList.Count-1; index >= 0 ; index --)
            if (AnimalList[index].OwnName == OwnName)
                AnimalList.RemoveAt(index)
                found = true
        if (found == false) { throw new AnimalNotExistException() }
    }
    def Birth(self):
        if (rnd.Next(0,100) > 90)
            if (AnimalList.Count > 0)
                int index = rnd.Next(0, AnimalList.Count)
                WriteLineGreen("A " + AnimalList[index].SpeciesName + " baby has born!")
                AddNewAnimal(AnimalList[index].SpeciesName, AnimalList[index].Type, AnimalList[index].IdealEnvironment)
    def Dying(self):
        if (rnd.Next(0, 100) > 98)
            if (AnimalList.Count > 50)
                int index = rnd.Next(0, AnimalList.Count)
                WriteLineRed("A " + AnimalList[index].SpeciesName + " has died!")
                AnimalList.RemoveAt(index)