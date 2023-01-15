import numpy
import pyrosim.pyrosim as pyrosim
import constants as c

class SENSOR:

    def __init__(self, linkName):
        
        self.linkName = linkName
        self.Prepare_To_Sense()

    def Prepare_To_Sense(self):
        self.values = numpy.zeros(c.simlength)

    def Get_Value(self, timeStep):
        self.values[timeStep] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)     
        # if timeStep >= (c.simlength-1):   
        #     print(self.values)

    def Save_Values(self):
        fileLoc = "data/" + str(self.linkName) + "SensorData.npy"
        numpy.save(fileLoc, self.values)