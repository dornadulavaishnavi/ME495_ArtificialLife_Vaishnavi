# import pybullet as p
# import pybullet_data
# import pyrosim.pyrosim as pyrosim
# import numpy
# import time
# import math
# import random
# import matplotlib.pylab as plt
# import constants as c

# physicsClient = p.connect(p.GUI)
# p.setAdditionalSearchPath(pybullet_data.getDataPath())

# p.setGravity(0,0,-9.8)
# planeId = p.loadURDF("plane.urdf")
# robotId = p.loadURDF("body.urdf")
# p.loadSDF("world.sdf")

# pyrosim.Prepare_To_Simulate(robotId)

# backLegSensorValues = numpy.zeros(c.simlength)
# frontLegSensorValues = numpy.zeros(c.simlength)

# targetAngles = numpy.linspace(0, 2*numpy.pi, c.simlength)
# targetAngles_backLeg = c.amplitude_backLeg * numpy.sin(c.frequency_backLeg*targetAngles + c.phaseOffset_backLeg) # numpy.sin(targetAngles)*(numpy.pi/4)
# targetAngles_frontLeg = c.amplitude_frontLeg * numpy.sin(c.frequency_frontLeg*targetAngles + c.phaseOffset_frontLeg) 
# # numpy.save("data/targetAngles.npy", targetAngles)


# for i in range(c.simlength):
#     p.stepSimulation()
#     backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#     frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
#     pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b'Torso_BackLeg', controlMode = p.POSITION_CONTROL, targetPosition = targetAngles_backLeg[i], maxForce = c.maximum_force)
#     pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b'Torso_FrontLeg', controlMode = p.POSITION_CONTROL, targetPosition = targetAngles_frontLeg[i], maxForce = c.maximum_force)
#     time.sleep(c.simSleepTime)
#     # print(i)

# # print(backLegSensorValues)
# numpy.save("data/backLegSensordata.npy", backLegSensorValues)
# numpy.save("data/frontLegSensordata.npy", frontLegSensorValues)

# p.disconnect() 

from simulation import SIMULATION

simulation = SIMULATION()