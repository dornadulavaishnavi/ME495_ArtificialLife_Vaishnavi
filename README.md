# ME495 Artificial Life Assignment 7 Winter 2023

## Generate Random 3D Snake
## Author: Vaishnavi Dornadula
## Last Editted: February 20th, 2023

### Relevant Files to Run Assignment 7 (Changed from Ludobots Final Project)
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
- This assignment is hosted on the 'assignment7' branch of this repo.
- There are multiple ways to clone this project:
    1. To get the clone key, click on the green 'code' button in the upper right side of the repo. Then copy the html or ssh key given under the 'local' tab depending on your security preferences
    2. 'git clone ssh-or-html-key' will clone the whole repo and will automatically start in the main branch. To switch branches, use git switch or git checkout to move to the finalproject branch
    3. alternatively to step 2, 'git clone -b my-branch git@github.com:user/myproject.git' will clone a particular branch of the repo, where in this case, 'my-branch' should be 'finalproject' and 'git@github.com:user/myproject.git' should be the clone key you obtained in step 1

- Once the repo is cloned, run 'python .\randomSnake.py'. Depending on your system and python installations, your 'python' may be 'python3' or 'py'.

### How it Generates Random Snakes in Three Dimensions
The solution class constructor creates a random number between 1 and 6 (inclusive) to determine the number of links the snake's vertebrae will contain. The code has similar logic to assignment 6 in which we generate a single dimention snake that extends in the x direction. The description for how that single chain snake is created is at the end of this section. In the Generate_Body() function, I set up a number of nested for loops that I incrementaly coded. First, I started with one vertebrae and added legs to one side in the y direction. I constrain the legs the randomly choose to be outwards or downwards and generate a random number of them between 0 and 5. This allows the spine block to have legs in the x and z directions. The for loop that generates these random legs from a given spine block first randomly generates the direction, then creates the joint at the correct position, accounting for if the previous block was outwards or downwards. These leg blocks are also constrained to be within the size of its related spine block to avoid self collisions with other blocks. Each leg block is placed relative to the previous but since the first leg block is connected to the root, its coordinates were absolute. This for loop is then repeated to generate a new random number of legs on the other side of the spine block. Once this was working with the randomly generated sensor and motor neurons in the same fashion as assignment 6, I had a robot with a single center body and random legs being generated in the x and z directions. Next I encapsulated that nested for loop into another to generate more vertebrae with legs, allowing the snake to grow in the y direction as well. This for loop created a new vertebrae block and made the random legs for either side for how many ever random links were created in the solution class constructor. The second link to the spine was specified in absolute coordinates since it was connected to the root but all others were relative to the vertebrae before. Each set of legs was linked to its vertebrae so that it would hopefully be able to move like a weird centipede. This meant there were a lot more variables to track from assignment 6 which is why the for loops are much longer. 

How single chain snakes were constructed in Assignment 6:
The solution class constructor creates a random number between 1 and 6 (inclusive) to determine the number of links the snake will contain. The class also contains a Generate_Body() function which is called in the Evaluate() function which will then generate that number of links sequentially with joints in between. The first block is the root block and every subsequent link is a child to the previous block, meaning that only the second joint and link are in absolute coordinates, the rest are relative. This can be confirmed by looking at the body.urdf file where each link is named "Cube" and then some number ID that is concatanated to it to create unique names. Each time a link is created, I generate a random number, 0 or 1, to determine if it will have a sensor and if so, the name is saved in a list. I do this again with each joint to determine which will have motors. These lists are then used in the Generate_Brain() function called in Evaluate() to assign the sensors, motors, and synapses. I also editted pyrosim's Send_Cube() function to take a parameter indicating if it is a sensor or not so I can change its material to reflect that.

### Diagram of Joints and Links
This diagram shows how the links and joints are related for a three 'vertebrae' snake in three dimensions and breifly explains the brain.

![3d_block_relations](https://user-images.githubusercontent.com/90789243/220213684-99a7cfd8-1234-4b51-9384-c86d5c4bdbf7.png)

### Video 
In this assignment, we generate bodies in three dimensions with a random number of links where each of these links are also a random shape. Then we assign sensors to random links as well and I assigned random joints to also have a motor. Line 137 of the solution.py file specifies that the joint type created for the motors will always be the 0th index of the joint_list variable. Changing the 0 to the commented line that's on the same line will randomize the type of joint generated between those two cubes. I changed this to 0 because it was difficult to tell if my robot had self collisions or if there was a prismatic joint, but users are welcome to change that back. The brain0.nndf file in the background of the videos shows the sensor and motor neurons randomly generated tied to each snake. This file gets deleted at the end of the run so it is only visible while the solution runs on the simulation.

The 10 second sped up video is at: https://youtu.be/fhXsssr4iD4

The real time video can be found at: https://youtu.be/IIpcKTCkEZM

#### This project was created by following the Ludobots course on Reddit
#### Assigned by Dr. Kriegman at Northwestern University
