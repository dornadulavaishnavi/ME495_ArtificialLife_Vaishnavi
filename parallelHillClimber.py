import copy
from solution import SOLUTION
import constants as c

class PARALLEL_HILL_CLIMBER: 

    def __init__(self):
        self.parents = {}
        self.nextAvailableID = 0
        for pop in range(c.populationSize):
            self.parents[pop] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

        # print(self.parents)

    def Evolve(self):
        for parent in self.parents:
            self.parents[parent].Start_Simulation("GUI")

        for parent in self.parents:
            self.parents[parent].Wait_For_Simulation_To_End()
            
        # for currentGeneration in range(c.numberOfGenerations):
        #     self.Evolve_For_One_Generation()
        pass

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        # exit()
        self.Select()
        self.Print()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)
        self.child.Set_ID(self.nextAvailableID)
        self.nextAvailableID += 1

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

    def Show_Best(self):
        # self.parent.Evaluate("GUI")
        pass

    def Print(self):
        print("[" + str(self.parent.fitness) + ", " + str(self.child.fitness) + "]")