import matplotlib.pyplot as plt
import numpy
for i in range(100):
    x = numpy.random.rand() * 100
    y = numpy.random.rand() * 100
    plt.plot([x],[y],'ro')
plt.axis([0,100,0,100])
plt.ylabel('some numbers')
plt.show()