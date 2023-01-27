import numpy as np 

class SOLUTION: 

    def __init__(self):
        self.weight = np.zeros((3,2))
        for row in range(3):
            for column in range(2):
                self.weight[row][column] = np.random.rand()

        # print(self.weight)
        self.weight = self.weight*2-1
        # print(self.weight)
        # exit()
    
    def Evaluate(self):
        pass

    def Create_World():
        length = 1
        width = 1
        height = 1

        x = 2
        y = 2
        z = height/2

        pyrosim.Start_SDF("world.sdf")

        pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
        pyrosim.End()

    def Create_Body():
        Create_World()
        
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5] , size=[1.0,1.0,1.0])
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [1.0,0.0,1.0])
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0.0,-0.5] , size=[1,1,1])
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [2.0,0.0,1.0])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0.0,-0.5] , size=[1,1,1])
        
        pyrosim.End()

    def Create_Brain():
        pyrosim.Start_NeuralNetwork("brain.nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")

        for sensor in range(3):
            for motor in range(3,5):
                pyrosim.Send_Synapse( sourceNeuronName = sensor , targetNeuronName = motor , weight = random.randint(-1,1) )

        pyrosim.End()
