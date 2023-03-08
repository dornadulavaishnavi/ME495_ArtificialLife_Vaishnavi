import pybullet as p

class WORLD:

    def __init__(self):
        # pass

        self.planeId = p.loadURDF("plane.urdf")
        file_success_flag = 0
        while file_success_flag == 0:
            try:
                p.loadSDF("world.sdf")
                file_success_flag = 1
            except:
                pass