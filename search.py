import os

for run in range(5):
    os.system("python generate.py")
    os.system("python simulate.py")