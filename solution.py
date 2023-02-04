import numpy as np 
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c

class SOLUTION: 

    def __init__(self, ID):
        self.myID = ID
        self.weight = np.zeros((c.numSensorNeurons,c.numMotorNeurons))
        # for row in range(3):
        #     for column in range(2):
        #         self.weight[row][column] = np.random.rand()

        # print(self.weight)
        self.weight = self.weight*2-1
        # print(self.weight)
        # exit()
    
    def Evaluate(self, directOrGUI):
        self.Create_Body()
        self.Create_Brain()
        runString = "start /B python simulate.py " + directOrGUI + " " + str(self.myID)
        os.system(runString)

        fitnessFileName = "fitness" + str(self.myID) + ".txt"
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)
        f = open(fitnessFileName, "r")
        self.fitness = float(f.read())
        print(self.fitness)
        f.close()

    def Start_Simulation(self, directOrGUI):
        self.Create_Body()
        self.Create_Brain()
        runString = "start /B python simulate.py " + directOrGUI + " " + str(self.myID)
        os.system(runString)

    def Wait_For_Simulation_To_End(self):
        fitnessFileName = "fitness" + str(self.myID) + ".txt"
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)
        f = open(fitnessFileName, "r")
        self.fitness = float(f.read())
        # print(self.fitness)
        f.close()

        os.system("del " + fitnessFileName)

    def Create_World(self):
        # fitnessFileName = "fitness.txt"
        # while not os.path.exists(fitnessFileName):
        #     time.sleep(0.01)

        length = 1
        width = 1
        height = 1

        x = 2
        y = 2
        z = height/2

        pyrosim.Start_SDF("world.sdf")

        pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
        pyrosim.End()

    def Create_Body(self):
        # fitnessFileName = "fitness.txt"
        # while not os.path.exists(fitnessFileName):
        #     time.sleep(0.01)

        self.Create_World()
        jointAxisString = "0 1 0"
        jointAxisPrismaticString = "0 0 1"
        pyrosim.Start_URDF("body.urdf")

        # self.cube = {}
        # self.cube["Torso"] = {0.0,0.0,1.0,1.0,1.0,1.0}
        pyrosim.Send_Cube(name="Torso", pos=[0.0,0.0,2.0] , size=[1.0,1.0,1.0])

        # for leg in range(self.num_legs):
        #     cube_name = "Leg" + str(leg)

        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0.0,-0.5,2.0], jointAxis = jointAxisString)
        pyrosim.Send_Cube(name="BackLeg", pos=[0.0,-0.5,0.0] , size=[0.2,1,0.2])
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0.0,0.5,2.0], jointAxis = jointAxisString)
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.0,0.5,0.0] , size=[0.2,1,0.2])
        pyrosim.Send_Joint( name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , type = "revolute", position = [-0.5,0.0,2.0], jointAxis = jointAxisString)
        pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5,0.0,0.0] , size=[1,0.2,0.2])
        pyrosim.Send_Joint( name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , type = "revolute", position = [0.5,0.0,2.0], jointAxis = jointAxisString)
        pyrosim.Send_Cube(name="RightLeg", pos=[0.5,0.0,0.0] , size=[1,0.2,0.2])

        pyrosim.Send_Joint( name = "Torso_BackLowerLeg" , parent= "BackLeg" , child = "BackLowerLeg" , type = "revolute", position = [0.0,-1.0,0.0], jointAxis = jointAxisString)
        pyrosim.Send_Cube(name="BackLowerLeg", pos=[0.0,0.0,-0.5] , size=[0.2,0.2,1])
        pyrosim.Send_Joint( name = "Torso_FrontLowerLeg" , parent= "FrontLeg" , child = "FrontLowerLeg" , type = "revolute", position = [0.0,1.0,0.0], jointAxis = jointAxisString)
        pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0.0,0.0,-0.5] , size=[0.2,0.2,1])
        pyrosim.Send_Joint( name = "Torso_LeftLowerLeg" , parent= "LeftLeg" , child = "LeftLowerLeg" , type = "revolute", position = [-1.0,0.0,0.0], jointAxis = jointAxisString)
        pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0.0,0.0,-0.5] , size=[0.2,0.2,1])
        pyrosim.Send_Joint( name = "Torso_RightLowerLeg" , parent= "RightLeg" , child = "RightLowerLeg" , type = "revolute", position = [1.0,0.0,0.0], jointAxis = jointAxisString)
        pyrosim.Send_Cube(name="RightLowerLeg", pos=[0.0,0.0,-0.5] , size=[0.2,0.2,1])

        pyrosim.Send_Joint( name = "Lower_BackLowerLeg" , parent= "BackLowerLeg" , child = "BackLowerLowerLeg" , type = "prismatic", position = [0.0,0.0,-1.0], jointAxis = jointAxisPrismaticString)
        pyrosim.Send_Cube(name="BackLowerLowerLeg", pos=[0.0,0.0,-0.5] , size=[0.2,0.2,1])
        pyrosim.Send_Joint( name = "Lower_FrontLowerLeg" , parent= "FrontLowerLeg" , child = "FrontLowerLowerLeg" , type = "prismatic", position = [0.0,0.0,-1.0], jointAxis = jointAxisPrismaticString)
        pyrosim.Send_Cube(name="FrontLowerLowerLeg", pos=[0.0,0.0,-0.5] , size=[0.2,0.2,1])
        pyrosim.Send_Joint( name = "Lower_LeftLowerLeg" , parent= "LeftLowerLeg" , child = "LeftLowerLowerLeg" , type = "prismatic", position = [0.0,0.0,-1.0], jointAxis = jointAxisPrismaticString)
        pyrosim.Send_Cube(name="LeftLowerLowerLeg", pos=[0.0,0.0,-0.5] , size=[0.2,0.2,1])
        pyrosim.Send_Joint( name = "Lower_RightLowerLeg" , parent= "RightLowerLeg" , child = "RightLowerLowerLeg" , type = "prismatic", position = [0.0,0.0,-1.0], jointAxis = jointAxisPrismaticString)
        pyrosim.Send_Cube(name="RightLowerLowerLeg", pos=[0.0,0.0,-0.5] , size=[0.2,0.2,1])

        # make dictionary of joints and cubes
        # mutate: rand generate number of legs
        # assign joint positions in clockwise order and generate strings in loop
        # send joints and cubes
        # in create brain, loop through to send sensor and motor neurons and assign all to equal weight
        pyrosim.End()
        # exit()
        
    def Create_Brain(self):
        # fitnessFileName = "fitness.txt"
        # while not os.path.exists(fitnessFileName):
        #     time.sleep(0.01)

        brainFile = "brain" + str(self.myID) + ".nndf"
        pyrosim.Start_NeuralNetwork(brainFile)
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LeftLeg")
        pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "RightLeg")
        pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "FrontLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "BackLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 7 , linkName = "LeftLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 8 , linkName = "RightLowerLeg")
        pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons+1 , jointName = "Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons+2 , jointName = "Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons+3 , jointName = "Torso_RightLeg")
        pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons+4 , jointName = "Torso_FrontLowerLeg")
        pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons+5 , jointName = "Torso_BackLowerLeg")
        pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons+6 , jointName = "Torso_LeftLowerLeg")
        pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons+7 , jointName = "Torso_RightLowerLeg")
        pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons+8 , jointName = "Lower_BackLowerLeg")
        pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons+9 , jointName = "Lower_FrontLowerLeg")
        pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons+10 , jointName = "Lower_LeftLowerLeg")
        pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons+11 , jointName = "Lower_RightLowerLeg")

        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                self.weight[currentRow][currentColumn] = np.random.rand()
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+c.numSensorNeurons , weight = self.weight[currentRow][currentColumn])

        # for sensor in range(3):
        #     for motor in range(3,5):
        #         pyrosim.Send_Synapse( sourceNeuronName = sensor , targetNeuronName = motor , weight = random.randint(-1,1) )

        pyrosim.End()
        # exit()

    def Mutate(self):
        self.weight[random.randint(0,(c.numSensorNeurons-1))][random.randint(0,(c.numMotorNeurons-1))] = random.random()*2-1
        # self.num_legs = random.randint(1,8)

    def Set_ID(self, newID):
        self.myID = newID
