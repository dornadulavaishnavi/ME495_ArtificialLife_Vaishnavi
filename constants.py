import numpy

simlength = 1000
simSleepTime = 1/240

amplitude_backLeg = numpy.pi/4
frequency_backLeg = 10
phaseOffset_backLeg = -numpy.pi/8
amplitude_frontLeg = numpy.pi/2
frequency_frontLeg = 20
phaseOffset_frontLeg = numpy.pi/2

maximum_force = 75

numberOfGenerations = 3
populationSize = 3

numSensorNeurons = 10
numMotorNeurons = 9

motorJointRange = 0.3