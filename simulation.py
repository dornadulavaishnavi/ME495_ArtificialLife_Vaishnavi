import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
from world import WORLD
from robot import ROBOT
import constants as c
import time

class SIMULATION:

    def __init__(self):

        
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        p.setGravity(0,0,-9.8)        
        self.world = WORLD()
        self.robot = ROBOT()


    def Run(self):
        for i in range(c.simlength):
            p.stepSimulation()
            # backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
            # frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
            # pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b'Torso_BackLeg', controlMode = p.POSITION_CONTROL, targetPosition = targetAngles_backLeg[i], maxForce = c.maximum_force)
            # pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b'Torso_FrontLeg', controlMode = p.POSITION_CONTROL, targetPosition = targetAngles_frontLeg[i], maxForce = c.maximum_force)
            time.sleep(c.simSleepTime)
            # print(i)
    
    def __del__(self):
        p.disconnect()