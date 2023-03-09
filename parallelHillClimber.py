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

        fitness_file = "trial.csv"
        self.f = (open(fitness_file, "a"))
        # print(self.parents)

    def Evolve(self):
        # for parent in self.parents:
        #     self.parents[parent].Start_Simulation("DIRECT")

        # for parent in self.parents:
        #     self.parents[parent].Wait_For_Simulation_To_End()
        self.Evaluate(self.parents)
        self.Show_Best()

        for currentGeneration in range(c.numberOfGenerations):
            print("Current Generation being Evaluated: "+str(currentGeneration))
            self.Evolve_For_One_Generation()
            # self.Show_Best()
        self.f.close()

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
            # for gen in range(c.numberOfGenerations):
            if (self.parents[key].fitness > self.children[key].fitness):
                self.parents[key] = copy.deepcopy(self.children[key])
            self.f.write(str(self.parents[key].fitness)+",")
        self.f.write("\n")

    def Show_Best(self):
        best_parent_key = 0
        for parent in self.parents:
            if self.parents[best_parent_key].fitness > self.parents[parent].fitness:
                best_parent_key = parent
        print("Best Parent Fitness")
        print(self.parents[best_parent_key].fitness)
        # self.parents[best_parent_key].Start_Simulation("GUI")
        runString = "start /B python simulate.py GUI " + str(self.parents[best_parent_key].myID)
        os.system(runString)
        # body_file = "best_body_seed" + str(self.parents[best_parent_key].seed) + ".csv"
        # body_file = "brain" + str(self.parents[best_parent_key].myID) 
        # self.f = (open(fitness_file, "a"))

    def Evaluate(self, solutions):
        for solution in solutions:
            solutions[solution].Start_Simulation("DIRECT")

        for solution in solutions:
            solutions[solution].Wait_For_Simulation_To_End()

    def Print(self):
        for key in self.parents:
            # for gen in range(c.numberOfGenerations):
                print("\n[" + str(self.parents[key].fitness) + ", " + str(self.children[key].fitness) + "]\n")