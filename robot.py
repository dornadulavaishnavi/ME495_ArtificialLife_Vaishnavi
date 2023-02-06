import pybullet as p
import pyrosim.pyrosim as pyrosim
import os
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
import constants as c
class ROBOT:

    def __init__(self, solutionID):
        self.solutionID = solutionID

        self.robotId = p.loadURDF("body.urdf")
        self.blockID = p.loadURDF("block.urdf")
        self.nn = NEURAL_NETWORK("brain" + str(self.solutionID) + ".nndf")

        pyrosim.Prepare_To_Simulate(self.robotId)
        
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

        os.system("del brain" + str(self.solutionID) + ".nndf")

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)
        return

    def Sense(self, dt):
        for link in self.sensors:
            self.sensors[link].Get_Value(dt)
        return

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
        return

    def Act(self, dt):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
                self.motors[jointName.encode()].Set_Value(self.robotId, desiredAngle)
                # print(desiredAngle)
                # print(jointName)
                # print(neuronName)

        # for joint in self.motors:
        #     self.motors[joint].Set_Value(self.robotId, dt)
        return

    def Think(self):
        self.nn.Update()
        # self.nn.Print()
        
    # def Get_Fitness(self):
    #     # stateOfLinkZero = p.getLinkState(self.robotId,0)
    #     # positionOfLinkZero = stateOfLinkZero[0]
    #     # xCoordinateOfLinkZero = positionOfLinkZero[0]
    #     basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)
    #     basePosition = basePositionAndOrientation[0]
    #     xCoordinateOfLinkZero = basePosition[0]
    #     # print(xCoordinateOfLinkZero)
    #     fitnessString = "fitness"+ str(self.solutionID) + ".txt"
    #     tmpString = "tmp" + str(self.solutionID) + ".txt"

    #     f = (open(tmpString, "w"))
    #     f.write(str(xCoordinateOfLinkZero))
    #     # print("rename " + tmpString + " " + fitnessString)
    #     f.close()
    #     os.system("rename " + tmpString + " " + fitnessString)
    #     exit()

    def Get_Fitness(self):
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.blockID)
        basePosition = basePositionAndOrientation[0]
        xCoordinateOfLinkZero = basePosition[0]
        fitnessString = "fitness"+ str(self.solutionID) + ".txt"
        tmpString = "tmp" + str(self.solutionID) + ".txt"

        f = (open(tmpString, "w"))
        f.write(str(xCoordinateOfLinkZero))
        # print("rename " + tmpString + " " + fitnessString)
        f.close()
        os.system("rename " + tmpString + " " + fitnessString)
        exit()