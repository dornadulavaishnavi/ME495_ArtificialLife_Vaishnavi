import numpy
import matplotlib.pyplot

backLegSensor_data = numpy.load("data/backLegSensordata.npy")
frontLegSensor_data = numpy.load("data/frontLegSensordata.npy")
# targetAngle_data = numpy.load("data/targetAngles.npy")
# print(sensor_data)

# matplotlib.pyplot.plot(targetAngle_data, label = "Target Angle Data")
matplotlib.pyplot.plot(backLegSensor_data, label = 'Back Leg Sensor Data', linewidth = 3)
matplotlib.pyplot.plot(frontLegSensor_data, label = "Front Leg Sensor Data")

# matplotlib.pyplot.legend()
matplotlib.pyplot.show()