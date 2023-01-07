import pybullet as p

physicsClient = p.connect(p.GUI)

for i in range(100):
    p.stepSimulation()
    
p.disconnect() 