import pyrosim.pyrosim as pyrosim

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

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5] , size=[1.0,1.0,1.0])
    pyrosim.Send_Joint( name = "Torso_Back_Leg" , parent= "Torso" , child = "Back_Leg" , type = "revolute", position = [1.0,0.0,1.0])
    pyrosim.Send_Cube(name="Back_Leg", pos=[-0.5,0.0,-0.5] , size=[1,1,1])
    # pyrosim.Send_Joint( name = "Torso_Front_Leg" , parent= "Torso" , child = "Front_Leg" , type = "revolute", position = [0.5,0.0,-0.5])
    # pyrosim.Send_Cube(name="Front_Leg", pos=[0.5,0.0,-0.5] , size=[1,1,1])
    pyrosim.End()

def Create_Robot_Example():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Link0", pos=[0,0,0.5] , size=[1.0,1.0,1.0])
    pyrosim.Send_Joint( name = "Link0_Link1" , parent= "Link0" , child = "Link1" , type = "revolute", position = [0.0,0.0,1.0])
    pyrosim.Send_Cube(name="Link1", pos=[0.0,0.0,0.5] , size=[1,1,1])
    pyrosim.Send_Joint( name = "Link1_Link2" , parent= "Link1" , child = "Link2" , type = "revolute", position = [0.0,0.0,1.0])
    pyrosim.Send_Cube(name="Link2", pos=[0.0,0.0,0.5] , size=[1,1,1])
    pyrosim.Send_Joint( name = "Link2_Link3" , parent= "Link2" , child = "Link3" , type = "revolute", position = [0.0,0.5,0.5])
    pyrosim.Send_Cube(name="Link3", pos=[0.0,0.5,0.0] , size=[1,1,1])
    pyrosim.Send_Joint( name = "Link3_Link4" , parent= "Link3" , child = "Link4" , type = "revolute", position = [0.0,1.0,0.0])
    pyrosim.Send_Cube(name="Link4", pos=[0.0,0.5,0.0] , size=[1,1,1])
    pyrosim.End()

Create_World()
Create_Robot()