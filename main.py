# implement a libaries
import matplotlib.pyplot as plt
import numpy as np


# TODO: write number in arabic
# TODO: slim grid and graph from y side

# write number in arabic
def arabic_number(number, pos_x, pos_y):
    print(u"number")


draw_width = 2                          #TODO:control view
draw_height = 6
color_ = 'red'



draw_height += .5
draw_width += .5


def draw_arrows():
    # draw vertical arrow with red color
    plt.arrow(0, 0, 0, draw_height, color='red', head_width=0.2, head_length=0.2)
    plt.arrow(0, 0, 0, -1 * draw_height, color='red', head_width=0.2, head_length=0.2)

    # draw horizontal arrow with red color
    plt.arrow(0, 0, draw_width, 0, color='red', head_width=0.2, head_length=0.2)
    plt.arrow(0, 0, -1 * draw_width, 0, color='red', head_width=0.2, head_length=0.2)


# draw y = x^3+x with red color
x = np.arange(-1.8, 1.8, 0.01)

y = x  # put equation here
plt.plot(x, y, color=color_)

# plotting the points

draw_height += 2
draw_width += 2

# change mode two squares
plt.axis([-1 * draw_width, draw_width, -1 * draw_height, draw_height])
plt.grid(color=color_, linewidth=0.5)

resolution_value = 1200
plt.savefig("myImage.png", format="png", dpi=resolution_value)
plt.show()

# end of code

