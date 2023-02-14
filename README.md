# ME495 Artificial Life Assignment 6 Winter 2023

## Generate Random Snake
## Author: Vaishnavi Dornadula
## Last Editted: February 6th, 2023

### Relevant Files to Run Assignment 6 (Changed from Ludobots Final Project)
1. pyrosim -> material_normal.py: contains rgb and opacity values to change the visual appearance of the normal (non sensor) blocks
2. pyrosim -> material_sensor.py: contains rgb and opacity values to change the visual appearance of the sensor blocks
3. body.urdf: the description file for the robot body
4. brain.nndf: neural network description file containing the motor and sensor neurons
5. world.sdf: contains the world elements
6. constants.py: contains variables used across multiple files that remain unchanged 
7. motor.py: class that sets motor joint values
8. robot.py: handles the sensing and movement of a robot as well as evaluating its fitness
9. sensor.py: gets sensor values and saves them in data files
10. simulate.py: interfaces with simulation functions
11. simulation.py: runs the simulation in direct or gui mode
12. world.py: loads the world file 
13. randomSnake.py: the main file generates a solution and evaluates it with the GUI

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
The solution class constructor creates a random number between 1 and 10 (inclusive) to determine the number of links the snake will contain. The class also contains a Generate_Body() function which is called in the Evaluate() function which will then generate that number of links sequentially with joints in between. The first block is the root block and every subsequent link is a child to the previous block, meaning that only the second joint and link are in absolute coordinates, the rest are relative. This can be confirmed by looking at the body.urdf file where each link is named "Cube" and then some number ID that is concatanated to it to create unique names. Each time a link is created, I generate a random number, 0 or 1, to determine if it will have a sensor and if so, the name is saved in a list. I do this again with each joint to determine which will have motors. These lists are then used in the Generate_Brain() function called in Evaluate() to assign the sensors, motors, and synapses. I also editted pyrosim's Send_Cube() function to take a parameter indicating if it is a sensor or not so I can change its material to reflect that.

### Diagram of Joints and Links
This diagram shows how the links and joints are related for a four body snake for the x dimension. 
![block_relations](https://user-images.githubusercontent.com/90789243/218628878-37fb11a3-b796-45ad-8a9a-24e243989fc5.png)

### Embed Video 
In this assignment, we generate snakes with a random number of links where each of these links are also a random shape. Then we assign sensors to random links as well and I assigned random joints to also have a motor. The brain0.nndf file in the background of the videos shows the sensor and motor neurons randomly generated tied to each snake.

https://user-images.githubusercontent.com/90789243/218629281-c395bda7-d7c6-4d87-a500-5577bfe3d8e0.mp4

The real time video can be found at: https://youtu.be/W9ltSqaAxW0

#### This project was created by following the Ludobots course on Reddit
#### Assigned by Dr. Kriegman at Northwestern University
