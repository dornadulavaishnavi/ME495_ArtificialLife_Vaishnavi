import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import time
import math
import random
import matplotlib.pylab as plt

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

simlength = 1000
backLegSensorValues = numpy.zeros(simlength)
frontLegSensorValues = numpy.zeros(simlength)

amplitude_backLeg = numpy.pi/4
frequency_backLeg = 10
phaseOffset_backLeg = 0
amplitude_frontLeg = numpy.pi/4
frequency_frontLeg = 10
phaseOffset_frontLeg = 0

targetAngles = numpy.linspace(0, 2*numpy.pi, simlength)
targetAngles_backLeg = amplitude_backLeg * numpy.sin(frequency_backLeg*targetAngles + phaseOffset_backLeg) # numpy.sin(targetAngles)*(numpy.pi/4)
targetAngles_frontLeg = amplitude_frontLeg * numpy.sin(frequency_frontLeg*targetAngles + phaseOffset_frontLeg) 
# numpy.save("data/targetAngles.npy", targetAngles)


for i in range(simlength):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b'Torso_BackLeg', controlMode = p.POSITION_CONTROL, targetPosition = targetAngles_backLeg[i], maxForce = 50)
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b'Torso_FrontLeg', controlMode = p.POSITION_CONTROL, targetPosition = targetAngles_frontLeg[i], maxForce = 50)
    time.sleep((1/240))
    # print(i)

# print(backLegSensorValues)
numpy.save("data/backLegSensordata.npy", backLegSensorValues)
numpy.save("data/frontLegSensordata.npy", frontLegSensorValues)

p.disconnect() 