# ME495 Artificial Life Assignment 6 Winter 2023

## Generate Random Snake
## Author: Vaishnavi Dornadula
## Last Editted: February 6th, 2023

### Relevant Files to Run Assignment 6
1. pyrosim -> material.py: contains rgb and opacity values to change the color of the robot and block
2. pyrosim -> neuron.py: changed for quadruped to handle individual synapses
3. pyrosim -> neuralNetwork.py: changed for quadruped to hangle motors and other neurons
4. body.urdf: the description file for the robot body
5. block.urdf: the description file for the block
6. brain.nndf: neural network description file containing the motor and sensor neurons
7. world.sdf: contains the world elements
8. constants.py: contains variables used across multiple files that remain unchanged 
9. motor.py: class that sets motor joint values
10. parallelHillClimber.py: class that generates multiple parent and children solutions to mutate, evaluate, and select
11. robot.py: handles the sensing and movement of a robot as well as evaluating its fitness
12. search.py: the main file to run which calls functions from the parallelHillClimber class
13. sensor.py: gets sensor values and saves them in data files
14. simulate.py: interfaces with simulation functions
15. simulation.py: runs the simulation in direct or gui mode
16. solution.py: generates the world, robot body, brain, and block. Also contains the mutate function
17. world.py: loads the world file 

### Required installations to run code
- python3
- pybullet
- wheel (Optional for Windows Users)

### How to run the code
- This assignment is hosted on the 'assignment6' branch of this repo.
- There are multiple ways to clone this project:
    1. To get the clone key, click on the green 'code' button in the upper right side of the repo. Then copy the html or ssh key given under the 'local' tab depending on your security preferences
    2. 'git clone ssh-or-html-key' will clone the whole repo and will automatically start in the main branch. To switch branches, use git switch or git checkout to move to the finalproject branch
    3. alternatively to step 2, 'git clone -b my-branch git@github.com:user/myproject.git' will clone a particular branch of the repo, where in this case, 'my-branch' should be 'finalproject' and 'git@github.com:user/myproject.git' should be the clone key you obtained in step 1

- Once the repo is cloned, run 'python .\randomSnake.py'. Depending on your system and python installations, your 'python' may be 'python3' or 'py'.

### How it Generates Random Snakes


### Diagram of Joints and Links


### Embed Video 

https://user-images.githubusercontent.com/90789243/217118657-0714cb10-8379-41a7-97cf-2b0f761a88c7.mp4

The real time video can be found at: https://youtu.be/W9ltSqaAxW0

#### This project was created by following the Ludobots course on Reddit
#### Assigned by Dr. Kriegman at Northwestern University
