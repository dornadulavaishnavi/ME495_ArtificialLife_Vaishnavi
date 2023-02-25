import copy
import os
from solution import SOLUTION
import constants as c

class PARALLEL_HILL_CLIMBER: 

    def __init__(self):
        for pop in range(c.populationSize*c.numberOfGenerations):
            try:
                os.system("del brain" + str(pop) + ".nndf")
            except:
                pass
            try:
                os.system("del fitness" + str(pop) + ".txt")
            except:
                pass
            try:
                os.system("del body" + str(pop) + ".urdf")
            except:
                pass

        self.parents = {}
        self.nextAvailableID = 0
        for pop in range(c.populationSize):
            self.parents[pop] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

        # print(self.parents)

    def Evolve(self):
        # for parent in self.parents:
        #     self.parents[parent].Start_Simulation("DIRECT")

        # for parent in self.parents:
        #     self.parents[parent].Wait_For_Simulation_To_End()
        self.Evaluate(self.parents)

        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        # self.child.Evaluate("DIRECT")
        self.Evaluate(self.children)
        # exit()
        self.Select()
        self.Print()

    def Spawn(self):
        self.children = {}
        for parent in self.parents:
            self.children[parent] = copy.deepcopy(self.parents[parent])
            self.children[parent].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

        # print(self.children)
        # exit()

    def Mutate(self):
        for child in self.children:
            self.children[child].Mutate()
        # print(self.parent.weight)
        # print(self.child.weight)
        # exit()

    def Select(self):
        # print(self.parent.fitness)
        # print(self.child.fitness)
        # exit()
        for key in self.parents:
            for gen in range(c.numberOfGenerations):
                if (self.parents[key].fitness > self.children[gen].fitness):
                    self.parents[key] = copy.deepcopy(self.children[gen])

    def Show_Best(self):
        best_parent_key = 0
        for parent in self.parents:
            if self.parents[best_parent_key].fitness > self.parents[parent].fitness:
                best_parent_key = parent
        self.parents[c.numberOfGenerations-1].Start_Simulation("GUI")

    def Evaluate(self, solutions):
        for solution in solutions:
            solutions[solution].Start_Simulation("GUI")

        for solution in solutions:
            solutions[solution].Wait_For_Simulation_To_End()

    def Print(self):
        for key in self.parents:
            for gen in range(c.numberOfGenerations):
                print("\n[" + str(self.parents[key].fitness) + ", " + str(self.children[gen].fitness) + "]\n")