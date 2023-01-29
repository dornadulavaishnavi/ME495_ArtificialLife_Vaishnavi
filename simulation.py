import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
from world import WORLD
from robot import ROBOT
import constants as c
import time

class SIMULATION:

    def __init__(self, directOrGUI): 
        self.directOrGUI = directOrGUI
        if self.directOrGUI == "DIRECT":       
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)

        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        p.setGravity(0,0,-9.8)        
        self.world = WORLD()
        self.robot = ROBOT()


    def Run(self):
        for dt in range(c.simlength):
            p.stepSimulation()
            self.robot.Sense(dt)
            self.robot.Think()
            self.robot.Act(dt)
            if self.directOrGUI == "GUI":
                time.sleep(c.simSleepTime)
            # print(dt)
    
    def Get_Fitness(self):
        self.robot.Get_Fitness()

    def __del__(self):
        p.disconnect()