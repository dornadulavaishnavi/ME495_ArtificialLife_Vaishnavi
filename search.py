import os
from hillclimber import HILL_CLIMBER
from parallelHillClimber import PARALLEL_HILL_CLIMBER

phc = PARALLEL_HILL_CLIMBER()
# phc.Evolve()
# phc.Show_Best()
phc.Play_Specific(2986)

# for run in range(5):
#     os.system("python generate.py")
#     os.system("python simulate.py")