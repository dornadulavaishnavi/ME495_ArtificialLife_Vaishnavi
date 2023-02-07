# ME495 Artificial Life Ludobots Final Project (Assignment 5) Winter 2023

## Author: Vaishnavi Dornadula
## Last Editted: February 6th, 2023

### Contents of the repo
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
- This assignment is hosted on the 'finalproject' branch of this repo.
- There are multiple ways to clone this project:
    1. To get the clone key, click on the green 'code' button in the upper right side of the repo. Then copy the html or ssh key given under the 'local' tab depending on your security preferences
    2. 'git clone ssh-or-html-key' will clone the whole repo and will automatically start in the main branch. To switch branches, use git switch or git checkout to move to the finalproject branch
    3. alternatively to step 2, 'git clone -b my-branch git@github.com:user/myproject.git' will clone a particular branch of the repo, where in this case, 'my-branch' should be 'finalproject' and 'git@github.com:user/myproject.git' should be the clone key you obtained in step 1

- Once the repo is cloned, run 'python .\search.py'. Depending on your system and python installations, you 'python' may be 'python3' or 'py'.

### Fitness Function and Mutations

The robot's goal is to get the purple block to go as far to the right (out of the screen) as possible. I was hoping to see robot evolve to either hit the block with it's top 'horn' very hard or 'dribble' the block with it's legs further to the right. The mutate function changes a random leg to have a new random weight and along with that, changes the 'horn' attachment's weight to that same randomly generated value. The fitness function of the program checks to see how far the block has moved at the end of the simulation, that way the robot evolves to consistently move the block further and is 'penalized' for potentially bringing it back. This is checked by querying the block's x position and saving that as the fitness of that solution. Solutions that were able to move the block further to the right, signified by a larger positive value, were deemed the more successful.

### Changes made to the quadruped code to achieve desired functionality

Initially, the shape of the quadruped was editted to have 8 legs, 2 on each side, but this impeded the robot's locomotion, so I removed the extra legs and instead added a 'horn' on top that could swing and hit the block. I also created a new urdf file for the block itself so I could track its position to access in the fitness function. This block could not be added to the robot's body urdf file because there can only be 1 root element in each file and that would restrict the block to be attached to an existing robot element through a joint. The mutate function changed to affect 2 joints: 1 leg and the horn. To ensure there isn't too much randomness introduced, the same random value is assigned to both elements. An interesting bug that I believe to be an issue with the local system is it will not show the initial random solution if there are more than 8 generations and 8 memebers of the population. These values can be found in the constants file.

### Embed Video and Explain what is seen
In this video, the random robot solution has weak motions and knocks the block backwards but the evolved solution moves more purposefully, knocking the block forward initially and 'dribbling' it forward with more force to move it further out of the screen and to the right

#### This project was created by following the Ludobots course on Reddit
#### Assigned by Dr. Kriegman at Northwestern University