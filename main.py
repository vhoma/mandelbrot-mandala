import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
import numpy as np

# defaults
center = (0, 0)
radius = 1
dot_size = 0.01

# play with these
num_dots0 = 10
num_dots_min = 10
num_dots_max = 300

factor0 = 2
factor_min = 2
factor_max = 200

fig, ax = plt.subplots(figsize=(7, 7))
plt.subplots_adjust(left=0.175, right=0.825, bottom=0.25)
plt.axis([
    center[0] - radius - 0.2,
    center[0] + radius + 0.2,
    center[1] - radius - 0.2,
    center[1] + radius + 0.2
])

def draw(num_dots, factor, axes):
    # add main circle
    circle1 = plt.Circle(center, radius, color='blue', fill=False)
    axes.add_artist(circle1)

    # add dots on the circle
    dots = []
    for i in range(num_dots):
        angle = 2 * np.pi * i * (1.0 / num_dots)
        dot_coordinates = (np.cos(angle) * radius, np.sin(angle) * radius)
        dot = plt.Circle(dot_coordinates, dot_size, color='red')
        dots.append(dot_coordinates)
        axes.add_artist(dot)
        
    # add dots connections
    for i in range(len(dots)):
        d0 = dots[i]
        d1 = dots[(i * factor) % num_dots]
        axes.plot([d0[0], d1[0]],[d0[1], d1[1]],'g')
        
draw(num_dots0, factor0, ax)

################
# Set controls #
################
axcolor = 'lightgoldenrodyellow'

# Sliders
ax_numdots = plt.axes([0.175, 0.1, 0.65, 0.03], facecolor=axcolor)
ax_factor = plt.axes([0.175, 0.15, 0.65, 0.03], facecolor=axcolor)
slider_numdots = Slider(ax_numdots, 'NumDots', num_dots_min, num_dots_max, valinit=num_dots0, valfmt='%0.0f')
slider_factor = Slider(ax_factor, 'Factor', factor_min, factor_max, valinit=factor0, valfmt='%0.0f')

def update(val):
    ax.clear()
    num_dots = slider_numdots.val
    factor = slider_factor.val
    draw(int(num_dots), int(factor), ax)
    fig.canvas.draw()
slider_numdots.on_changed(update)
slider_factor.on_changed(update)

# +/- buttons
numdots_plus1_ax = plt.axes([0.880, 0.1, 0.03, 0.03])
button_numdots_plus1 = Button(numdots_plus1_ax, '+', color=axcolor, hovercolor='0.975')

def numdots_plus1(event):
    new_val = slider_numdots.val + 1
    if new_val > slider_numdots.valmax:
        new_val = slider_numdots.valmax
    slider_numdots.set_val(new_val)
button_numdots_plus1.on_clicked(numdots_plus1)

numdots_minus1_ax = plt.axes([0.025, 0.1, 0.03, 0.03])
button_numdots_minus1 = Button(numdots_minus1_ax, '-', color=axcolor, hovercolor='0.975')

def numdots_minus1(event):
    new_val = slider_numdots.val - 1
    if new_val < slider_numdots.valmin:
        new_val = slider_numdots.valmin
    slider_numdots.set_val(new_val)
button_numdots_minus1.on_clicked(numdots_minus1)

factor_plus1_ax = plt.axes([0.880, 0.15, 0.03, 0.03])
button_factor_plus1 = Button(factor_plus1_ax, '+', color=axcolor, hovercolor='0.975')

def factor_plus1(event):
    new_val = slider_factor.val + 1
    if new_val > slider_factor.valmax:
        new_val = slider_factor.valmax
    slider_factor.set_val(new_val)
button_factor_plus1.on_clicked(factor_plus1)

factor_minus1_ax = plt.axes([0.025, 0.15, 0.03, 0.03])
button_factor_minus1 = Button(factor_minus1_ax, '-', color=axcolor, hovercolor='0.975')

def factor_minus1(event):
    new_val = slider_factor.val - 1
    if new_val < slider_factor.valmin:
        new_val = slider_factor.valmin
    slider_factor.set_val(new_val)
button_factor_minus1.on_clicked(factor_minus1)


# reset button
resetax = plt.axes([0.725, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

def reset(event):
    slider_numdots.reset()
    slider_factor.reset()
button.on_clicked(reset)

# save picture button
save_ax = plt.axes([0.615, 0.025, 0.1, 0.04])
button_save = Button(save_ax, 'Save', color=axcolor, hovercolor='0.975')

def save(event):
    fig.savefig('plot.png')
button_save.on_clicked(save)


plt.show()
