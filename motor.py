import pybullet as p
import numpy
import pyrosim.pyrosim as pyrosim
import constants as c

class MOTOR:

    def __init__(self, jointName):

        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.values = numpy.zeros(c.simlength)
        self.amplitude = c.amplitude_backLeg
        self.frequency = c.frequency_backLeg
        self.offset = c.phaseOffset_backLeg
        
        self.motorValues = numpy.linspace(0, 2*numpy.pi, c.simlength)
        self.motorValues = self.amplitude * numpy.sin(self.frequency*self.motorValues + self.offset) # numpy.sin(targetAngles)*(numpy.pi/4)
        
    def Set_Value(self, robot, timeStep):
        pyrosim.Set_Motor_For_Joint(bodyIndex = robot, jointName = self.jointName, controlMode = p.POSITION_CONTROL, targetPosition = self.motorValues[timeStep], maxForce = c.maximum_force)

    def Save_Values(self):
        fileLoc = "data/" + str(self.linkName) + "MotorValues.npy"
        numpy.save(fileLoc, self.motorValues)
