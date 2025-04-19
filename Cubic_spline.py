import numpy 
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
arr = numpy.loadtxt('bps.dat')

x = arr[:, 0]  
y = arr[:, 1]  
cs = CubicSpline(x, y)

# Calculate the range of X values
x_min = numpy.min(x)
x_max = numpy.max(x)
X_ax = numpy.linspace(x_min, x_max, 1000)

Y_ax = cs(X)

# Plot the original arr points
plt.scatter(x, y, color='red', label='Original Data')

# Plot the interpolated function
plt.plot(X_ax, Y_ax, color='blue', label='Cubic spline interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Cubic Spline Interpolation of Data from bps.dat')
plt.legend()
plt.grid(True)
plt.show()
