import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1

x = 0
y = 0
z = height/2

pyrosim.Start_SDF("boxes.sdf")

loop_x = x  

for i in range(5):
    loop_y = y 
    loop_x = loop_x + length
    for j in range(5):
        loop_z = z 
        loop_length = length
        loop_width = width 
        loop_height = height
        loop_y = loop_y + loop_width
        for k in range(10):
            pyrosim.Send_Cube(name="Box", pos=[loop_x,loop_y,loop_z] , size=[loop_length,loop_width,loop_height])
            loop_z = loop_z + loop_height
            loop_length = loop_length*0.9
            loop_width = loop_width*0.9
            loop_height = loop_height*0.9
    
# pyrosim.Send_Cube(name="Box2", pos=[x+length,y,z+height] , size=[length,width,height])
pyrosim.End()
