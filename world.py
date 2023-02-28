import pybullet as p

class WORLD:

    def __init__(self):
        # pass

        self.planeId = p.loadURDF("plane.urdf")
        try:
            p.loadSDF("world.sdf")
        except:
            pass