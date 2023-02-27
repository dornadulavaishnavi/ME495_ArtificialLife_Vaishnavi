import numpy as np 
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c

class SOLUTION: 

    def __init__(self, ID):
        self.myID = ID
        self.weight = np.zeros((c.numSensorNeurons,c.numMotorNeurons))
        # for row in range(3):
        #     for column in range(2):
        #         self.weight[row][column] = np.random.rand()

        # print(self.weight)
        random.seed = 1
        self.weight = self.weight*2-1
        self.numLinks = 4 #random.randint(1,6)
        self.num_leg_extentions = 5 # random.randint(0,5)
        self.block_size = 1
        self.vert_cube_bound = [self.block_size/4,self.block_size/4,self.block_size/4] # random.uniform(0,self.block_size)
        self.direction_array = [random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)]
        # print(self.weight)
        # exit()
    
    def Evaluate(self, directOrGUI):
        self.Create_Body()
        self.Create_Brain()
        runString = "start /B python simulate.py " + directOrGUI + " " + str(self.myID)
        os.system(runString)

        fitnessFileName = "fitness" + str(self.myID) + ".txt"
        while not os.path.exists(fitnessFileName):
            time.sleep(0.05)
        f = open(fitnessFileName, "r")
        self.fitness = float(f.read())
        print(self.fitness)
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

        length = 1
        width = 1
        height = 1

        x = 2
        y = 2
        z = height/2

        pyrosim.Start_SDF("world.sdf")

        # pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
        pyrosim.End()

    def Create_Body(self):
        # fitnessFileName = "fitness.txt"
        # while not os.path.exists(fitnessFileName):
        #     time.sleep(0.01)

        self.Create_World()
        jointAxisString = "0 1 0"
        bodyFile = "body" + str(self.myID) + ".urdf"
        pyrosim.Start_URDF(bodyFile)
        
        low_bound = 0.2
        high_bound = 1.5
        

        joint_list = ["revolute","spherical","prismatic","fixed"]
        starting_height = 4

        self.links = []
        self.joints = []
        self.sensor_links = []
        self.motor_joints = []

        curIndex = 0
        baseString = "Cube"
        randX = self.block_size # random.uniform(low_bound,high_bound)
        randY = self.block_size # random.uniform(low_bound,high_bound)
        randZ = self.block_size # random.uniform(low_bound,high_bound)
        prev_vertX = randX
        prev_vertY = randY
        prev_vertZ = randZ
        prev_vertIndex = curIndex

        stringName = baseString + str(curIndex)
        sensor_flag = random.randint(0,1)
        pyrosim.Send_Cube(name=stringName, pos=[0.0,0.0,starting_height] , size=[randX,randY,randZ],sensor_flag=sensor_flag)
        self.links.append(stringName)
        if sensor_flag == 1:
            self.sensor_links.append(stringName)

        curIndex += 1

        xPrev = self.vert_cube_bound[0]
        yPrev = self.vert_cube_bound[1]
        zPrev = self.vert_cube_bound[2]

        
        dir_y = 1
        for cube in range(self.numLinks):
            for side in range(2):
                dir_y = dir_y*-1
                # print("Number of extensions "+str(self.num_leg_extentions))
                xPrev = prev_vertX
                yPrev = prev_vertY
                zPrev = prev_vertZ
                for extension in range(self.num_leg_extentions):
                    randX = self.vert_cube_bound[0] # random.uniform(low_bound,self.vert_cube_bound)
                    randY = self.vert_cube_bound[1] # random.uniform(low_bound,self.vert_cube_bound)
                    randZ = self.vert_cube_bound[2] # random.uniform(low_bound,self.vert_cube_bound)

                    direction = self.direction_array[extension] # random.randint(0,1)
                    sensor_flag = random.randint(0,1)
                    motor_flag = 1 # random.randint(0,1)
                    joint_type = 0 # random.randint(0,3)

                    if extension == 0:
                        prevStringName = baseString + str(prev_vertIndex)
                        stringName = baseString + str(curIndex)
                        jointName = str(prevStringName) + "_" + stringName
                        if cube == 0:
                            pyrosim.Send_Joint( name = jointName , parent= prevStringName , child = stringName , type = joint_list[joint_type], position = [0.0,dir_y*prev_vertY/2,starting_height], jointAxis = jointAxisString)
                        else:
                            pyrosim.Send_Joint( name = jointName , parent= prevStringName , child = stringName , type = joint_list[joint_type], position = [-dir_y*prev_vertX/2,dir_y*prev_vertY/2,starting_height], jointAxis = jointAxisString)
                        pyrosim.Send_Cube(name=stringName, pos=[0.0,dir_y*randY/2,0.0] , size=[randX,randY,randZ],sensor_flag=sensor_flag)
                        prev_dir = 0
                    else:
                        prevStringName = baseString + str(curIndex-1)
                        stringName = baseString + str(curIndex)
                        jointName = str(prevStringName) + "_" + stringName
                        if direction == 0:
                            if prev_dir == 0:
                                pyrosim.Send_Joint( name = jointName , parent= prevStringName , child = stringName , type = joint_list[joint_type], position = [0.0,dir_y*yPrev,0.0], jointAxis = jointAxisString)
                            else:
                                pyrosim.Send_Joint( name = jointName , parent= prevStringName , child = stringName , type = joint_list[joint_type], position = [0.0,dir_y*yPrev/2,-zPrev/2], jointAxis = jointAxisString)
                            pyrosim.Send_Cube(name=stringName, pos=[0.0,dir_y*randY/2,0.0] , size=[randX,randY,randZ],sensor_flag=sensor_flag)
                            prev_dir = 0
                        elif direction == 1:
                            if prev_dir == 0:
                                pyrosim.Send_Joint( name = jointName , parent= prevStringName , child = stringName , type = joint_list[joint_type], position = [0.0,dir_y*yPrev/2,-zPrev/2], jointAxis = jointAxisString)
                            else:
                                pyrosim.Send_Joint( name = jointName , parent= prevStringName , child = stringName , type = joint_list[joint_type], position = [0.0,0.0,-zPrev], jointAxis = jointAxisString)
                            pyrosim.Send_Cube(name=stringName, pos=[0.0,0.0,-randZ/2] , size=[randX,randY,randZ],sensor_flag=sensor_flag)
                            prev_dir = 1
                    
                    self.links.append(stringName)
                    self.joints.append(jointName)
                    if sensor_flag == 1:
                        self.sensor_links.append(stringName)
                    if motor_flag == 1:
                        self.motor_joints.append(jointName)

                    xPrev = randX
                    yPrev = randY
                    zPrev = randZ
                    curIndex +=1
            
            if cube < (self.numLinks-1):
                randX = self.block_size # random.uniform(low_bound,high_bound)
                randY = self.block_size # random.uniform(low_bound,high_bound)
                randZ = self.block_size # random.uniform(low_bound,high_bound)

                prevStringName = baseString + str(prev_vertIndex)
                stringName = baseString + str(curIndex)
                jointName = str(prevStringName) + "_" + stringName
                motor_flag = 1 # random.randint(0,1)
                if cube == 0:
                    # absolute version
                    pyrosim.Send_Joint( name = jointName , parent= prevStringName , child = stringName , type = "revolute", position = [prev_vertX/2,0.0,starting_height], jointAxis = jointAxisString)
                else:
                    pyrosim.Send_Joint( name = jointName , parent= prevStringName , child = stringName , type = "revolute", position = [prev_vertX,0.0,0.0], jointAxis = jointAxisString)
                self.joints.append(jointName)
                if motor_flag == 1:
                    self.motor_joints.append(jointName)

                sensor_flag = random.randint(0,1)
                pyrosim.Send_Cube(name=stringName, pos=[randX/2,0.0,0.0] , size=[randX,randY,randZ],sensor_flag=sensor_flag)
                self.links.append(stringName)
                if sensor_flag == 1:
                    self.sensor_links.append(stringName)

                prev_vertX = randX
                prev_vertY = randY
                prev_vertZ = randZ
                xPrev = self.vert_cube_bound[0]
                yPrev = self.vert_cube_bound[1]
                zPrev = self.vert_cube_bound[2]
                prev_vertIndex = curIndex
                starting_height = 0.0
                curIndex +=1

            # break

        pyrosim.End()
        
    def Create_Brain(self):
        # fitnessFileName = "fitness.txt"
        # while not os.path.exists(fitnessFileName):
        #     time.sleep(0.01)

        brainFile = "brain" + str(self.myID) + ".nndf"
        pyrosim.Start_NeuralNetwork(brainFile)
        # print("creating brain file")

        sensor_index = 0
        for link in self.sensor_links:
            pyrosim.Send_Sensor_Neuron(name = sensor_index , linkName = link)
            sensor_index += 1

        motor_index = sensor_index
        for joint in self.motor_joints:
            pyrosim.Send_Motor_Neuron( name = motor_index , jointName = joint)
            motor_index += 1

        for sensor in range(sensor_index):
            for motor in range(len(self.motor_joints)):
                pyrosim.Send_Synapse( sourceNeuronName = sensor , targetNeuronName = motor+sensor_index-1 , weight = random.random()*2-1)
                # pyrosim.Send_Synapse( sourceNeuronName = sensor , targetNeuronName = motor+sensor_index-1 , weight = 1)

        pyrosim.End()
        # exit()

        # fitnessFileName = "fitness.txt"
        # while not os.path.exists(fitnessFileName):
        #     time.sleep(0.01)

        # brainFile = "brain" + str(self.myID) + ".nndf"
        # pyrosim.Start_NeuralNetwork(brainFile)
        # pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        # pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        # pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        # pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LeftLeg")
        # pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "RightLeg")
        # pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "FrontLowerLeg")
        # pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "BackLowerLeg")
        # pyrosim.Send_Sensor_Neuron(name = 7 , linkName = "LeftLowerLeg")
        # pyrosim.Send_Sensor_Neuron(name = 8 , linkName = "RightLowerLeg")
        # pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons , jointName = "Torso_BackLeg")
        # pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons+1 , jointName = "Torso_FrontLeg")
        # pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons+2 , jointName = "Torso_LeftLeg")
        # pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons+3 , jointName = "Torso_RightLeg")
        # pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons+4 , jointName = "Torso_FrontLowerLeg")
        # pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons+5 , jointName = "Torso_BackLowerLeg")
        # pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons+6 , jointName = "Torso_LeftLowerLeg")
        # pyrosim.Send_Motor_Neuron( name = c.numSensorNeurons+7 , jointName = "Torso_RightLowerLeg")

        # for currentRow in range(c.numSensorNeurons):
        #     for currentColumn in range(c.numMotorNeurons):
        #         self.weight[currentRow][currentColumn] = np.random.rand()
        #         pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+c.numSensorNeurons , weight = self.weight[currentRow][currentColumn])

        # for sensor in range(3):
        #     for motor in range(3,5):
        #         pyrosim.Send_Synapse( sourceNeuronName = sensor , targetNeuronName = motor , weight = random.randint(-1,1) )

        # pyrosim.End()
        # exit()

    def Mutate(self):
        # self.weight[random.randint(0,(c.numSensorNeurons-1))][random.randint(0,(c.numMotorNeurons-1))] = random.random()*2-1
        random_mutate = random.randint(0,2)
        self.vert_cube_bound[random_mutate] = random.uniform(0,self.block_size)
        # self.direction_array[random_mutate] = ~self.direction_array[random_mutate]

    def Set_ID(self, newID):
        self.myID = newID
