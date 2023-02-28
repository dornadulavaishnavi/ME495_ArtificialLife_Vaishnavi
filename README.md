# ME495 Artificial Life Assignment 8 Winter 2023

## Evolve 3D Snake
## Author: Vaishnavi Dornadula
## Last Editted: February 27th, 2023

### Relevant Files to Run Assignment 8 (Changed from Ludobots Final Project)
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
13. search.py: the main file generates a parallel hill climber class object and evaluates it for the number of generations/populations specified in constants.py

### Required installations to run code
- python3
- pybullet
- wheel (Optional for Windows Users)

### How to run the code
- This assignment is hosted on the 'assignment8_v3' branch of this repo.
- There are multiple ways to clone this project:
    1. To get the clone key, click on the green 'code' button in the upper right side of the repo. Then copy the html or ssh key given under the 'local' tab depending on your security preferences
    2. 'git clone ssh-or-html-key' will clone the whole repo and will automatically start in the main branch. To switch branches, use git switch or git checkout to move to the assignment8_v3 branch
    3. alternatively to step 2, 'git clone -b my-branch git@github.com:user/myproject.git' will clone a particular branch of the repo, where in this case, 'my-branch' should be 'assignment8_v3' and 'git@github.com:user/myproject.git' should be the clone key you obtained in step 1

- Once the repo is cloned, run 'python .\search.py'. Depending on your system and python installations, your 'python' may be 'python3' or 'py'.

### How the Robots are Created and Evolved
Below is the explaination for how random snakes were generated in 3 dimensions. For this assignment, we took these 3d snakes and evolved them. The fitness function I chose was to see how to move the snake further in the negative x direction. The way my robot is generated remains in the same loop format at assignment 7 but I set many of the variables to be a fixed number as to not have too many random factors in play for evolution. The 'vertebrae' of the snake is set to 4 links long and each link has a pair of legs that are 5 links long. These links are set up to be in a random direction. For example, a random direction array or [0,1,0,0,1] means that the legs will be outward, downward, out, out, and down. each of its children will have this same leg set up but the mutation function allows these legs to change. The mutation function chooses a dimension at random (x,y,z) and changes that dimension for the leg to be that random number. The brain is generated from the sensor links that are specified and the motors. The synapses are generated between all the elements with a random weight. 

How random snakes were created in Assignment 7: The solution class constructor creates a random number between 1 and 6 (inclusive) to determine the number of links the snake's vertebrae will contain. The code has similar logic to assignment 6 in which we generate a single dimention snake that extends in the x direction. The description for how that single chain snake is created is at the end of this section. In the Generate_Body() function, I set up a number of nested for loops that I incrementaly coded. First, I started with one vertebrae and added legs to one side in the y direction. I constrain the legs the randomly choose to be outwards or downwards and generate a random number of them between 0 and 5. This allows the spine block to have legs in the x and z directions. The for loop that generates these random legs from a given spine block first randomly generates the direction, then creates the joint at the correct position, accounting for if the previous block was outwards or downwards. These leg blocks are also constrained to be within the size of its related spine block to avoid self collisions with other blocks. Each leg block is placed relative to the previous but since the first leg block is connected to the root, its coordinates were absolute. This for loop is then repeated to generate a new random number of legs on the other side of the spine block. Once this was working with the randomly generated sensor and motor neurons in the same fashion as assignment 6, I had a robot with a single center body and random legs being generated in the x and z directions. Next I encapsulated that nested for loop into another to generate more vertebrae with legs, allowing the snake to grow in the y direction as well. This for loop created a new vertebrae block and made the random legs for either side for how many ever random links were created in the solution class constructor. The second link to the spine was specified in absolute coordinates since it was connected to the root but all others were relative to the vertebrae before. Each set of legs was linked to its vertebrae so that it would hopefully be able to move like a weird centipede. This meant there were a lot more variables to track from assignment 6 which is why the for loops are much longer.

### Fitness Curves
The plots shown below show the fitness curves of 5 different runs, each with a different random seed specified in the solution.py file's constructor. The best fitness in each generation is saved into a file called 'fitness_seed#.csv' where the number is the random seed that was set. The assignment asks us to do many more populations and generations than I was able to acheive here due to time constraints and my laptop overheating. I plan to solve this issue before the final project so I can run much larger generation and population sizes. The x axis shows the generation number and the y shows the fitness. Since I was trying to get the robot to move further in the negative x direction, the downward curve of the graphs shows how the fitness gets better in each generation. The multiple dots of different colors at each generation represent the best member of each population.


### Diagram of Joints and Links
These diagrams show how the links and joints are related for the four 'vertebrae' snake in three dimensions and breifly explains the brain.

### Video 
In this assignment, we generate bodies in three dimensions with a 4 links of a set size and set number of legs which are in random directions. The mutation will change the size of 1 dimension chosen at random to a new random number within a bound. Then we assign sensors to random links as well and I assigned all joints to also have a motor. Line 137 of the solution.py file specifies that the joint type created for the motors will always be the 0th index of the joint_list variable. Changing the 0 to the commented line that's on the same line will randomize the type of joint generated between those two cubes. I changed this to 0 because it was difficult to tell if my robot had self collisions or if there was a prismatic joint, but users are welcome to change that back. It was interesting to see the different ways the robot evolved, whether it be towards more effective gait or just taller legs that made it fall far in the desired direction.

The 10 second sped up video is at: 

The real time video can be found at: 

#### This project is based on the Ludobots course on Reddit
#### Assigned by Dr. Kriegman at Northwestern University