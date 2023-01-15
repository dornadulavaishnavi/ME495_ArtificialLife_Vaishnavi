import numpy
import pyrosim.pyrosim as pyrosim
import constants as c

class MOTOR:

    def __init__(self, jointName):

        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.values = numpy.zeros(c.simlength)
        # pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b'Torso_BackLeg', controlMode = p.POSITION_CONTROL, targetPosition = targetAngles_backLeg[i], maxForce = c.maximum_force)
        # pyrosim.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b'Torso_FrontLeg', controlMode = p.POSITION_CONTROL, targetPosition = targetAngles_frontLeg[i], maxForce = c.maximum_force)
