import pyrosim.pyrosim as pyrosim

def Create_World():
    length = 1
    width = 1
    height = 1

    x = 0
    y = 0
    z = height/2

    pyrosim.Start_SDF("world.sdf")

    pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])

    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Link0", pos=[0,0,0.5] , size=[1.0,1.0,1.0])
    pyrosim.Send_Joint( name = "Link0_Link1" , parent= "Link0" , child = "Link1" , type = "revolute", position = [0.0,0.0,1.0])
    pyrosim.Send_Cube(name="Link1", pos=[0.0,0.0,0.5] , size=[1,1,1])
    pyrosim.End()

Create_World()
Create_Robot()