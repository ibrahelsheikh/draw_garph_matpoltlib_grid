import numpy as np
import matplotlib.pyplot as plt

## sample data
x = np.arange(10)
y1 = np.cos(x)
y2 = np.sin(x)
y3 = np.tan(x)
y4 = 1 / y3

## make easy to identify
labels = ('cos', 'sin', 'tan', r'$\frac{1}{tan}$')
facecolors = ('darkorange', 'steelblue', 'purple', 'green')

## initialize plot
# fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12,7)) ## shape=(2,2)
fig, axes = plt.subplots(nrows=4, ncols=1, figsize=(12,7)) ## shape=(4,)
# fig, axes = plt.subplots(nrows=1, ncols=4, figsize=(12,7)) ## shape=(4,)

## verify shape of axes
print(axes.shape)

## create a plot
for ax, y, label, facecolor in zip(axes.ravel(), (y1, y2, y3, y4), labels, facecolors):
    ax.plot(x, y, label=label, color=facecolor)

## add legend
fig.subplots_adjust(bottom=0.2)
fig.legend(loc='lower center', mode='expand', fontsize=8, ncol=4)

## fig.nrows outputs AttributeError: 'Figure' object has no attribute 'nrows'.

## show and close
plt.show()
plt.close(fig)