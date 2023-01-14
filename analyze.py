import numpy
import matplotlib.pyplot

backLegSensor_data = numpy.load("data/backLegSensordata.npy")
frontLegSensor_data = numpy.load("data/frontLegSensordata.npy")
# print(sensor_data)

matplotlib.pyplot.plot(backLegSensor_data, label = 'Back Leg Sensor Data')
matplotlib.pyplot.plot(frontLegSensor_data, label = "Front Leg Sensor Data")

matplotlib.pyplot.legend()
matplotlib.pyplot.show()