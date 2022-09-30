# implement a libaries
import matplotlib.pyplot as plt
import numpy as np


# TODO: write number in arabic
# TODO: slim grid and graph from y side



draw_width = 2                          #TODO:control view
draw_height = 6

draw_height += .5
draw_width += .4


def draw_arrows():
    # draw vertical arrow with red color
    plt.arrow(0, 0, 0, draw_height, color='red', head_width=0.1, head_length=0.2)
    plt.arrow(0, 0, 0, -1 * draw_height, color='red', head_width=0.1, head_length=0.2)

    # draw horizontal arrow with red color
    plt.arrow(0, 0, draw_width, 0, color='red', head_width=0.2, head_length=0.1)
    plt.arrow(0, 0, -1 * draw_width, 0, color='red', head_width=0.2, head_length=0.1)

draw_arrows()
# draw y = x^3+x with red color
x = np.arange(-1.8, 1.8, 0.01)

y = x  # put equation here
plt.plot(x, y, color='red')

# plotting the points

draw_height +=.5
draw_width += .2

# change mode two squares
plt.axis([-1 * draw_width, draw_width, -1 * draw_height, draw_height])
plt.grid(color='red', linewidth=0.5)

resolution_value = 512
plt.savefig("myImage.png", format="png", dpi=resolution_value)


# Selecting the axis-X making the bottom and top axes False.
plt.tick_params(axis='x', which='both', bottom=False,
                top=False, labelbottom=False)

# Selecting the axis-Y making the right and left axes False
plt.tick_params(axis='y', which='both', right=False,
                left=False, labelleft=False)

# Iterating over all the axes in the figure
# and make the Spines Visibility as False
for pos in ['right', 'top', 'bottom', 'left']:
    plt.gca().spines[pos].set_visible(False)

resolution_value = 512
plt.savefig("myImage.png", format="png", dpi=resolution_value)
plt.show()

# end of code

