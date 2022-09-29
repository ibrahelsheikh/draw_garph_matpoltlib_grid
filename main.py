# implement a libaries
import matplotlib.pyplot as plt
import numpy as np

draw_width = 6
draw_height = 6

draw_height += .5
draw_width += .5

# draw vertical arrow with red color
plt.arrow(0, 0, 0, draw_height, color='red', head_width=0.2, head_length=0.2)
plt.arrow(0, 0, 0, -1 * draw_height, color='red', head_width=0.2, head_length=0.2)

# draw horizontal arrow with red color
plt.arrow(0, 0, draw_width, 0, color='red', head_width=0.2, head_length=0.2)
plt.arrow(0, 0, -1 * draw_width, 0, color='red', head_width=0.2, head_length=0.2)

# draw y = x^3+x
x = np.arange(-draw_width, draw_width, 0.01)
y = x ** 3 + x
plt.plot(x, y)





# plotting the points
plt.plot(x, y)

draw_height += 2
draw_width += 2

# change mode two squares
plt.axis([-1 * draw_width, draw_width, -1 * draw_height, draw_height])


plt.grid(color='red', linewidth=0.5)

resolution_value = 1200
plt.savefig("myImage.png", format="png", dpi=resolution_value)
plt.show()

# end of code
