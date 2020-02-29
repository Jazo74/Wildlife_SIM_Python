import ToolBox
import os
import time
import HabitatIsExistException
import HabitatNotExistException
import AnimalNotExistException
import NotEmptyHabitatException
import FileNotExistException
import Animal

class UI:
    life = ISimulation
    def __init__(self, sim):
        life = sim
    
    
    def SubChoiceHabitat(self, p):
        choice: str = ToolBox.InputAny("Choose an option: ")
        print()
        if choice == "1": # Creating new habitat
            try:
                newName: str = ToolBox.InputAny("The name of the new Habitat?: ")
                if p.arkOne.IsHabitatExist(newName):
                    raise HabitatIsExistException
                p.arkOne.CreatingAHabitat(newName)
                ToolBox.WriteLineGreen("Tha habitat has been built.")
            except HabitatIsExistException:
                ToolBox.WriteLineRed("This Habitat is already exist")
            time.Sleep(1500)
        elif choice == "2": # Displaying Habitats
            for habitat in p.arkOne.GetHabitats():
                ToolBox.WriteBlue(habitat.HabitatName + ": ")
                print(habitat.AnimalList.Count.ToString() + " animals live in this Habitat.")
            ToolBox.InputAny("Press any key to continue...")
        elif choice == "3": # Renaming a Habitat
            try:
                habitatName: str = ToolBox.InputAny("The name of the Habitat?: ")
                newName: str = ToolBox.InputAny("The new name of the Habitat?: ")
                if p.arkOne.IsHabitatExist(newName):
                    raise HabitatIsExistException()
                habitats = p.arkOne.GetHabitats()
                for habitat in habitats:
                    if not p.arkOne.IsHabitatExist(newName):
                        habitat.SetHabitatName(newName)
                        ToolBox.WriteLineGreen("The Habitat has been renamed.")
            except HabitatNotExistException:
                ToolBox.WriteLineRed("This Habitat is not exist")
            except HabitatIsExistException:
                ToolBox.WriteLineRed("This Habitat is already exist")
            time.sleep(1500)
        elif choice == "4": # Deleting a Habitat
            try:
                p.arkOne.RemovingAHabitat(ToolBox.InputAny("The name of the habitat?: "))
                ToolBox.WriteLineGreen("The Habitat has been demolished.")
            except HabitatNotExistException:
                ToolBox.WriteLineRed("This Habitat is not exist")
            except NotEmptyHabitatException:
                ToolBox.WriteLineRed("You can not demolish because animals live there")
            time.sleep(1500)
        elif choice == "0": # Back to main menu
            return False
        else:
            ToolBox.WriteLineRed("Wrong option!")
        return True
    def SubChoiceAnimal(self, p):
        choice = ToolBox.InputAny("Choose an option: ")
        print()
        if choice == "1": # Adding new animals
            typeo: str = ""
            speciesName = ToolBox.InputAny("What is the species?: ")
            habitatName = ToolBox.InputAny("What is the optimal habitat zone?: ")
            while True:
                typeo = ToolBox.InputAny("What kind of animal is this? (herbivore, carnivore, omnivore): ")
                if typeo.ToLower() == "herbivore" or typeo.ToLower() == "carnivore" or typeo.ToLower() == "omnivore":
                    break
            specimen: int = ToolBox.InputInt("How many animals arrived?: ")
            try:
                for count in range(specimen):
                    p.arkOne.AddNewAnimal(speciesName, type, habitatName)
            except HabitatNotExistException:
                ToolBox.WriteLineRed("This Habitat is not exist. You should build it first!");
                time.Sleep(1500)
        elif choice == "2": #Listing an animal
            animaL: Animal
            try:
                animaL = p.arkOne.FindAnimal(ToolBox.InputAny("What is the ID of the animal?: "))
                print("The animal ID is: " + animaL.OwnName)
                print("The animal species is: " + animaL.SpeciesName)
                print("Required energy: " + animaL.ReqEnergyUnit)
                print("Required heat: " + animaL.ReqHeatUnit)
                print("Required oxigen: " + animaL.ReqOxigenUnit)
                print("Required water: " + animaL.ReqWaterUnit)
                print("Required food: " + animaL.ReqFoodUnit)
            except AnimalNotExistException:
                ToolBox.WriteLineRed("There is no such animal...")
            ToolBox.InputAny("Press any key to continue...")
        elif choice == "3": #Listing all animal
            for habitat in p.arkOne.GetHabitats():
                ToolBox.WriteLineBlue(habitat.HabitatName)
                for animal in habitat.AnimalList:
                    print("ID: " + animal.OwnName.PadRight(4))
                    print(" " + animal.SpeciesName.PadRight(15))
                    print(" RE: " + animal.ReqEnergyUnit)
                    print(" RH: " + animal.ReqHeatUnit)
                    print(" RO: " + animal.ReqOxigenUnit)
                    print(" RW: " + animal.ReqWaterUnit)
                    print(" RF: " + animal.ReqFoodUnit)
            print("Press any key to continue...")
            ToolBox.InputAny()
        elif choice == "4": #Update an animal
            try:
                animaL = p.arkOne.FindAnimal(ToolBox.InputAny("What is the ID of the animal?: "))
                print("The animal ID is: " + animaL.OwnName)
                print("The animal species is: " + animaL.SpeciesName)
                print("Required energy: " + animaL.ReqEnergyUnit)
                print("Required heat: " + animaL.ReqHeatUnit)
                print("Required oxigen: " + animaL.ReqOxigenUnit)
                print("Required water: " + animaL.ReqWaterUnit)
                print("Required food: " + animaL.ReqFoodUnit)
                print()
                ToolBox.WriteLineRed("The parameters should be between 1 and 4")
                print()
                animaL.ReqEnergyUnit = ToolBox.InputIntBetween("New required energy?: ", 1, 4)
                animaL.ReqHeatUnit = ToolBox.InputIntBetween("New required heat ?: ", 1, 4)
                animaL.ReqOxigenUnit = ToolBox.InputIntBetween("New required oxigen?: ", 1, 4)
                animaL.ReqWaterUnit = ToolBox.InputIntBetween("New required water?: ", 1, 4)
                animaL.ReqFoodUnit = ToolBox.InputIntBetween("New required food?: ", 1, 4)
                print("The parameters of this animal has updated")
            except AnimalNotExistException:
                ToolBox.WriteLineRed("There is no such animal...")
            time.Sleep(1500)
        elif choice == "5": #Removing an animal
            try:
                p.arkOne.RelocateAnimal(ToolBox.InputAny("What is the ID of the animal you want to relocate?: "))
                ToolBox.WriteLineGreen("The animal has relocated.")
            except AnimalNotExistException:
                ToolBox.WriteLineRed("There is no such animal...")
            time.Sleep(1500)
        elif choice == "0":
            return False
        else:
            ToolBox.WriteLineRed("Wrong option!")
        return True
    def SubChoiceStatistics(self, p):
        choice: str = ""
        choice = ToolBox.InputAny("Choose an option: ")
        print()
        if choice == "1":
            for habitat in p.arkOne.GetHabitats():
                habitat.SumAnimals()
                ToolBox.WriteBlue(habitat.HabitatName)
                count: int = 0
                for items in habitat.AnimalDict:
                    count += items.Value
                print(" has " + count + " amimals")
            print()
            ToolBox.InputAny("Press any key to continue...")
        elif choice == "2":
            for habitat in p.arkOne.GetHabitats():
                habitat.SumAnimals()
                ToolBox.WriteLineBlue(habitat.HabitatName.ToUpper() + ":")
                for items in habitat.AnimalDict:
                    print(items.Keys + " : ")
                    print(items.Value)
            ToolBox.InputAny("Press any key to continue...")
        elif choice == "0":
            return False
        else:
            ToolBox.WriteLineRed("Wrong option!")
        return True
    def StarterPopulation(self, p):
        counter:int = 0
        while counter < 10:
            try:
                p.arkOne.AddNewAnimal("Tiger", "Carnivore", "Rainforest")
                p.arkOne.AddNewAnimal("Panda", "Herbivore", "Rainforest")
                p.arkOne.AddNewAnimal("Chimp", "Omnivore", "Rainforest")
                p.arkOne.AddNewAnimal("Zebra", "Herbivore", "Savannah")
                p.arkOne.AddNewAnimal("Lion", "Carnivore", "Savannah")
                p.arkOne.AddNewAnimal("Antilop", "Herbivore", "Savannah")
                p.arkOne.AddNewAnimal("Wolf", "Carnivore", "Temperate Forest")
                p.arkOne.AddNewAnimal("Beaver", "Herbivore", "Temperate Forest")
                p.arkOne.AddNewAnimal("Bald Eagle", "Carnivore", "Temperate Forest")
                p.arkOne.AddNewAnimal("Polar bear", "Carnivore", "Arctic")
                p.arkOne.AddNewAnimal("Seal", "Carnivore", "Arctic")
                p.arkOne.AddNewAnimal("Penguin", "Carnivore", "Arctic")
                p.arkOne.AddNewAnimal("Dolphin", "Carnivore", "Sea")
                p.arkOne.AddNewAnimal("Turtle", "Herbivore", "Sea")
                p.arkOne.AddNewAnimal("Seagull", "Herbivore", "Sea")
                counter += 1
            except HabitatNotExistException:
                ToolBox.WriteLineRed("Habitat is not exist!")
                time.Sleep(1500)
    def Menu(self): # main menu 
        os.system("clear")
        ToolBox.WriteLineBlue("Welcome to SANCTUARY, the last hope of the animals!")
        print()
        print("Hibernation status    ")
        if os.path.Exists("sanctuary.xml") == False:
            ToolBox.WriteLineRed("Not available")
        else:
            ToolBox.WriteLineGreen("Available")
        print()
        print("(1) Managing Habitat zones")
        print("(2) Managing life forms")
        print("(3) Live Monitoring")
        print("(4) Hibernating process")
        print("(5) Awakening process")
        print("(6) Statistics panel")
        print("(7) About US")
        print("(0) Exit Program")
        print()
    def SubMenuHabitat(self):
        os.system("clear")
        ToolBox.WriteLineBlue("Habitat panel (please choose a number)")
        print()
        print("(1) Building a new Habitat zone")
        print("(2) Information about the current zones")
        print("(3) Recalibrating the zones")
        print("(4) Demolish a zone")
        print("(0) Back to the main panel")
        print()
    def SubMenuAnimal(self):
        os.system("clear")
        ToolBox.WriteLineBlue("Animals panel (please choose a number)")
        print()
        print("(1) New animals has arrived")
        print("(2) Informations about an animal")
        print("(3) Informations about all animal")
        print("(4) Update the informations of the animal")
        print("(5) Relocating an animal")
        print("(0) Back to the main panel")
        print()
    def SubMenuStatistics(self):
        os.system("clear")
        ToolBox.WriteLineBlue("Statistics panel (please choose a number)")
        print()
        print("(1) Information about the Habitats")
        print("(2) Information about the animals")
        print("(0) Back to the main panel")
        print()
    def Choice(self, p, life):
            choice = ToolBox.InputAny("Choose an option: ")
            if choice == "1":
                loopH: bool = True
                while loopH:
                    SubMenuHabitat()
                    loopH = SubChoiceHabitat(p)
            elif choice == "2": # Animals submenu
                loopA: bool = True
                while loopA:
                    SubMenuAnimal()
                    loopA = SubChoiceAnimal(p)
            elif choice == "3": # Simulation
                cycleTime: int = ToolBox.InputInt("The cycles in miliseconds: ")
                life.LifeCycle(p,cycleTime)
            elif choice == "4": # Serialization
                p.arkOne.SerializeMyList()
                ToolBox.WriteLineGreen("The Serialization has completed.")
                os.Sleep(1500)
            elif choice == "5": # Deserialization
                try:
                    p.arkOne.DeSerializeMyList()
                    ToolBox.WriteLineGreen("The DeSerialization has completed.")
                except FileNotExistException:
                    ToolBox.WriteLineRed("The file not exist!")
                time.sleep(1500)
            elif choice == "6": # Statistics submenu
                loopS: bool = True
                while loopS:
                    SubMenuStatistics()
                    loopS = SubChoiceStatistics(p)
            elif choice == "7":
                os.system("Clear")
                StreamReader streamReader = new StreamReader("Readme.md")
                while not streamReader.EndOfStream:
                    print(streamReader.ReadLine())
                ToolBox.InputAny("Press any key to continue...")
                return True
            elif choice == "0": # Exit program
                ToolBox.WriteLineGreen("Thank you for using our service! Have a nice day citizen!")
                return False
            else:
                ToolBox.WriteLineRed("Wrong option!")
                return True
    def Start(self, p):
        StarterPopulation(p)
        loop: bool = True
        while loop:
            Menu()
            loop = Choice(p,life)