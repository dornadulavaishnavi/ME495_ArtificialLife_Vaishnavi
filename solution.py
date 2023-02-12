import numpy as np 
import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data
import os
import random
import time
import constants as c

class SOLUTION: 

    def __init__(self, ID):
        self.myID = ID
        self.weight = np.zeros((c.numSensorNeurons,c.numMotorNeurons))

        # physicsClient = p.connect(p.GUI)
        # p.setAdditionalSearchPath(pybullet_data.getDataPath())
        # p.setGravity(0,0,-9.8) 

        # for row in range(3):
        #     for column in range(2):
        #         self.weight[row][column] = np.random.rand()

        # print(self.weight)
        self.weight = self.weight*2-1
        # print(self.weight)
        # exit()
        self.numLinks = random.randint(1,10)
        print("Number of Links Expected "+str(self.numLinks))
    
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
        # print(self.fitness)
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

        # length = 1
        # width = 1
        # height = 1

        # x = 2
        # y = 2
        # z = height/2

        pyrosim.Start_SDF("world.sdf")

        # pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
        pyrosim.End()

    def Create_Body(self):
        # fitnessFileName = "fitness.txt"
        # while not os.path.exists(fitnessFileName):
        #     time.sleep(0.01)

        self.Create_World()
        jointAxisString = "0 1 0"
        pyrosim.Start_URDF("body.urdf")
        
        self.links = []
        self.joints = []

        curIndex = 0
        baseString = "Cube"
        randX = random.uniform(0.5,2.0)
        randY = random.uniform(0.5,2.0)
        randZ = random.uniform(0.5,2.0)
        xPrev = randX/2
        yPrev = randY/2
        zPrev = randZ/2

        stringName = baseString + str(curIndex)
        pyrosim.Send_Cube(name=stringName, pos=[0.0,0.0,randZ] , size=[randX,randY,randZ])
        self.links.append(stringName)

        curIndex += 1

        if self.numLinks > 1:
            # absolute coordinates
            randX = random.uniform(0.5,2.0)
            randY = random.uniform(0.5,2.0)
            randZ = random.uniform(0.5,2.0)

            prevStringName = baseString + str(curIndex-1)
            stringName = baseString + str(curIndex)
            jointName = str(prevStringName) + "_" + stringName
            pyrosim.Send_Joint( name = jointName , parent= prevStringName , child = stringName , type = "revolute", position = [xPrev/2,0.0,zPrev], jointAxis = jointAxisString)
            self.joints.append(jointName)

            pyrosim.Send_Cube(name=stringName, pos=[(xPrev/2)+(randX/2),0.0,zPrev] , size=[randX,randY,randZ])
            # p.changeVisualShape(1, 0, rgbaColor=[0.8, 0.6, 0.4, 1])
            self.links.append(stringName)

            xPrev = randX/2
            yPrev = randY/2
            zPrev = randZ/2
            curIndex +=1


        for cube in range(self.numLinks-2):
            randX = random.uniform(0.5,2.0)
            randY = random.uniform(0.5,2.0)
            randZ = random.uniform(0.5,2.0)

            prevStringName = baseString + str(curIndex-1)
            stringName = baseString + str(curIndex)
            jointName = str(prevStringName) + "_" + stringName
            pyrosim.Send_Joint( name = jointName , parent= prevStringName , child = stringName , type = "revolute", position = [xPrev,0.0,0.0], jointAxis = jointAxisString)
            self.joints.append(jointName)

            pyrosim.Send_Cube(name=stringName, pos=[(xPrev)+(randX/2),0.0,0.0] , size=[randX,randY,randZ])
            self.links.append(stringName)

            xPrev = randX/2
            yPrev = randY/2
            zPrev = randZ/2
            curIndex +=1

        pyrosim.End()
        # pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [0.0,-0.5,1.0], jointAxis = jointAxisString)
        # pyrosim.Send_Cube(name="BackLeg", pos=[0.0,-0.5,0.0] , size=[0.2,1,0.2])
        # pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [0.0,0.5,1.0], jointAxis = jointAxisString)
        # pyrosim.Send_Cube(name="FrontLeg", pos=[0.0,0.5,0.0] , size=[0.2,1,0.2])
        # pyrosim.Send_Joint( name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , type = "revolute", position = [-0.5,0.0,1.0], jointAxis = jointAxisString)
        # pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5,0.0,0.0] , size=[1,0.2,0.2])
        # pyrosim.Send_Joint( name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , type = "revolute", position = [0.5,0.0,1.0], jointAxis = jointAxisString)
        # pyrosim.Send_Cube(name="RightLeg", pos=[0.5,0.0,0.0] , size=[1,0.2,0.2])

        # pyrosim.Send_Joint( name = "Torso_BackLowerLeg" , parent= "BackLeg" , child = "BackLowerLeg" , type = "revolute", position = [0.0,-1.0,0.0], jointAxis = jointAxisString)
        # pyrosim.Send_Cube(name="BackLowerLeg", pos=[0.0,0.0,-0.5] , size=[0.2,0.8,1])
        # pyrosim.Send_Joint( name = "Torso_FrontLowerLeg" , parent= "FrontLeg" , child = "FrontLowerLeg" , type = "revolute", position = [0.0,1.0,0.0], jointAxis = jointAxisString)
        # pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0.0,0.0,-0.5] , size=[0.2,0.8,1])
        # pyrosim.Send_Joint( name = "Torso_LeftLowerLeg" , parent= "LeftLeg" , child = "LeftLowerLeg" , type = "revolute", position = [-1.0,0.0,0.0], jointAxis = jointAxisString)
        # pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0.0,0.0,-0.5] , size=[0.2,0.8,1])
        # pyrosim.Send_Joint( name = "Torso_RightLowerLeg" , parent= "RightLeg" , child = "RightLowerLeg" , type = "revolute", position = [1.0,0.0,0.0], jointAxis = jointAxisString)
        # pyrosim.Send_Cube(name="RightLowerLeg", pos=[0.0,0.0,-0.5] , size=[0.2,0.8,1])

        # pyrosim.Send_Joint( name = "Torso_HittingLeg" , parent= "Torso" , child = "HittingLeg" , type = "revolute", position = [0.0,0.0,1.5], jointAxis = "0 1 0")
        # pyrosim.Send_Cube(name="HittingLeg", pos=[0.0,0.0,0.0] , size=[0.2,0.2,1])

        # self.Create_Block()
        # exit()
    
    def Create_Block(self):
        pyrosim.Start_URDF("block.urdf")
        length = 0.5
        width = 0.5
        height = 0.5

        x = 0
        y = 0
        z = 2.5

        # pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
        pyrosim.End()

    def Create_Brain(self):
        # fitnessFileName = "fitness.txt"
        # while not os.path.exists(fitnessFileName):
        #     time.sleep(0.01)

        brainFile = "brain" + str(self.myID) + ".nndf"
        pyrosim.Start_NeuralNetwork(brainFile)
        # print("creating brain file")

        sensor_index = 0
        num_neurons = random.randint(0,(len(self.links)-1))
        valid_spot_flag = 0
        self.sensor_links = []
        for link in range(num_neurons):
            valid_spot_flag = 0
            while valid_spot_flag == 0:
                index = random.randint(0,num_neurons)
                if index in self.sensor_links:
                    valid_spot_flag = 0
                else:
                    pyrosim.Send_Sensor_Neuron(name = sensor_index , linkName = self.links[index])
                    sensor_index += 1
                    self.sensor_links.append(link)
                    valid_spot_flag = 1

        # pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        # pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        # pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        # pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LeftLeg")
        # pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "RightLeg")
        # pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "FrontLowerLeg")
        # pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "BackLowerLeg")
        # pyrosim.Send_Sensor_Neuron(name = 7 , linkName = "LeftLowerLeg")
        # pyrosim.Send_Sensor_Neuron(name = 8 , linkName = "RightLowerLeg")
        # pyrosim.Send_Sensor_Neuron(name = 9 , linkName = "HittingLeg")
        # # pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons , jointName = "Torso_BackLeg")
        # # pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons+1 , jointName = "Torso_FrontLeg")
        # # pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons+2 , jointName = "Torso_LeftLeg")
        # # pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons+3 , jointName = "Torso_RightLeg")
        # # pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons+4 , jointName = "Torso_FrontLowerLeg")
        # # pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons+5 , jointName = "Torso_BackLowerLeg")
        # # pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons+6 , jointName = "Torso_LeftLowerLeg")
        # # pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons+7 , jointName = "Torso_RightLowerLeg")
        # # pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons+8 , jointName = "Torso_HittingLeg")

        # for currentRow in range(c.numSensorNeurons):
        #     for currentColumn in range(c.numMotorNeurons):
        #         self.weight[currentRow][currentColumn] = np.random.rand()
        #         pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+c.numSensorNeurons , weight = self.weight[currentRow][currentColumn])

        # for sensor in range(3):
        #     for motor in range(3,5):
        #         pyrosim.Send_Synapse( sourceNeuronName = sensor , targetNeuronName = motor , weight = random.randint(-1,1) )

        pyrosim.End()
        # exit()

    def Mutate(self):
        mutate_random = random.random()*2-1
        self.weight[random.randint(0,(c.numSensorNeurons-1))][random.randint(0,(c.numMotorNeurons-1))] = mutate_random
        self.weight[8][8] = mutate_random*2

    def Set_ID(self, newID):
        self.myID = newID
