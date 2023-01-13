import numpy
import matplotlib.pyplot

sensor_data = numpy.load("data/backLegSensordata.npy")
# print(sensor_data)

matplotlib.pyplot.plot(sensor_data)
matplotlib.pyplot.show()