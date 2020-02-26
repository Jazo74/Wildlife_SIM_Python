import random
#[Serializable]
class Animal(base_species):
    ID: int
    def __init__ (self,SpeciesName, Type, IdealEnvironment):
        ID += 1
        super().IDOwnName = self.ID.ToString()
        super().SpeciesName = SpeciesName
        super().Type = Type
        super().IdealEnvironment = IdealEnvironment
        super().ReqHeatUnit = random.randint(1, 5)
        super().ReqOxigenUnit = random.raint(1, 5)
        super().ReqFoodUnit = random.randint(1, 5)
        super().ReqWaterUnit = random.randint(1, 5)
        super().ReqEnergyUnit = random.randint(1, 5)

