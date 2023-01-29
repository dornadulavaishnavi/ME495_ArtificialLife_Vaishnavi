import copy
from solution import SOLUTION
import constants as c

class HILL_CLIMBER: 

    def __init__(self):
        self.parent = SOLUTION()

    def Evolve(self):
        self.parent.Evaluate("DIRECT")

        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        # exit()
        self.Select()
        self.Print()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()
        # print(self.parent.weight)
        # print(self.child.weight)
        # exit()

    def Select(self):
        # print(self.parent.fitness)
        # print(self.child.fitness)
        # exit()
        if (self.parent.fitness > self.child.fitness):
            self.parent = self.child

    def Print(self):
        print("[" + str(self.parent.fitness) + ", " + str(self.child.fitness) + "]")