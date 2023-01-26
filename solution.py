import numpy as np 

class SOLUTION: 

    def __init__(self):
        self.weight = np.zeros((3,2))
        for row in range(3):
            for column in range(2):
                self.weight[row][column] = np.random.rand()

        print(self.weight)
        exit()
