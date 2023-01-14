import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import time
import math
import random

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

import matplotlib.pylab as plt
targetAngles = numpy.linspace(0, 2*numpy.pi, simlength)
targetAngles = numpy.sin(targetAngles)
numpy.save("data/targetAngles.npy", targetAngles)
# plt.plot(targetAngles, numpy.sin(targetAngles))

for i in range(simlength):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b'Torso_BackLeg', controlMode = p.POSITION_CONTROL, targetPosition = random.uniform(-math.pi/2, math.pi/2), maxForce = 50)
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b'Torso_FrontLeg', controlMode = p.POSITION_CONTROL, targetPosition = random.uniform(-math.pi/2, math.pi/2), maxForce = 50)
    time.sleep((1/200))
    # print(i)

# print(backLegSensorValues)
numpy.save("data/backLegSensordata.npy", backLegSensorValues)
numpy.save("data/frontLegSensordata.npy", frontLegSensorValues)

p.disconnect() 