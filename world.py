import pybullet as p

class WORLD:

    def __init__(self):
        # pass

        self.planeId = p.loadURDF("plane.urdf")
        p.loadSDF("world.sdf")
        # p.loadURDF("block.urdf")