# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                                                    app.__main__.py |
# |                                                                                             Author: Pauliv, Rômulo |
# |                                                                                          email: romulopauliv@bk.ru |
# |                                                                                                    encoding: UTF-8 |
# +--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from classes.particle import Particle
from classes.force import Force
# |--------------------------------------------------------------------------------------------------------------------|


p1: Particle = Particle((-5, 1), 1)
p2: Particle = Particle((0, 8.6602540), 1)
p3: Particle = Particle((5, 1), 1)

p1.define_init_velocity((0, 0))
p2.define_init_velocity((0, 0))
p3.define_init_velocity((0, 0))


for _ in range(0, 200):
    force_12: Force = Force(p1.get_particle(), p2.get_particle())
    force_13: Force = Force(p1.get_particle(), p3.get_particle())
    force_23: Force = Force(p2.get_particle(), p3.get_particle())

    p3.define_force(force_13.get_p2_force())
    p3.define_force(force_23.get_p2_force())

    p1.define_force(force_13.get_p1_force())    
    p1.define_force(force_12.get_p1_force())

    p2.define_force(force_23.get_p1_force())
    p2.define_force(force_12.get_p2_force())



    p1.update_frame(0.01)
    p2.update_frame(0.01)
    p3.update_frame(0.01)




import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

def init():
    ax.plot([], [], color="green", label='P1')
    ax.plot([], [], color="red", label='P2')
    ax.plot([], [], color="blue", label='P3')
    
    min_x: float = min(min(p1.x_list), min(p2.x_list), min(p3.x_list))
    max_x: float = max(max(p1.x_list), max(p2.x_list), max(p3.x_list))
    
    min_y: float = min(min(p1.y_list), min(p2.y_list), min(p3.y_list))
    max_y: float = max(max(p1.y_list), max(p2.y_list), max(p3.y_list))
    
    ax.set_xlim(min_x, max_x)
    ax.set_ylim(min_y, max_y)
    ax.grid(visible=True)
    return ax

def animate(frame):
    ax.lines[0].set_data(p1.x_list[:frame], p1.y_list[:frame])
    ax.lines[1].set_data(p2.x_list[:frame], p2.y_list[:frame])
    ax.lines[2].set_data(p3.x_list[:frame], p3.y_list[:frame])
    return ax

ani = FuncAnimation(fig, animate, frames=len(p1.x_list), init_func=init, blit=False, interval=1)

plt.show()