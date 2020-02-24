import random
#[Serializable]
class Animal:
    ID: int
    #rand = Random()
    OwnName: str
    SpeciesName: str # Tiger, Eagle
    Type: str #carnivore, herbivore, omnivore
    IdealEnvironment: str # Tropical, Arctic
    ReqHeatUnit: int
    ReqOxigenUnit: int
    ReqFoodUnit: int
    ReqWaterUnit: int
    ReqEnergyUnit: int
    # Constructor
    def __init__ (self):
        pass
    def __init__ (self,SpeciesName, Type, IdealEnvironment):
        ID += 1
        OwnName = ID.ToString()
        ReqHeatUnit = random.randint(1, 5)
        ReqOxigenUnit = random.raint(1, 5)
        ReqFoodUnit = random.randint(1, 5)
        ReqWaterUnit = random.randint(1, 5)
        ReqEnergyUnit = random.randint(1, 5)
        this.SpeciesName = SpeciesName
        this.Type = Type
        this.IdealEnvironment = IdealEnvironment

