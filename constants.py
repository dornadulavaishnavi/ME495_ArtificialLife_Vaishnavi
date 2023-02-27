import numpy

simlength = 1000
simSleepTime = 1/240

amplitude_backLeg = numpy.pi/4
frequency_backLeg = 10
phaseOffset_backLeg = -numpy.pi/8
amplitude_frontLeg = numpy.pi/2
frequency_frontLeg = 20
phaseOffset_frontLeg = numpy.pi/2

maximum_force = 100

numberOfGenerations = 10
populationSize = 5

numSensorNeurons = 9
numMotorNeurons = 8

motorJointRange = 0.4