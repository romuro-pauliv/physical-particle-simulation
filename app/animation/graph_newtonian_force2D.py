# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                                             app.animation.graph.py |
# |                                                                                             Author: Pauliv, Rômulo |
# |                                                                                          email: romulopauliv@bk.ru |
# |                                                                                                    encoding: UTF-8 |
# +--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from classes.particle.particle2D import Particle

from typing import Union
# |--------------------------------------------------------------------------------------------------------------------|


class MakeGraph(object):
    def __init__(self, particle_list: list[Particle]) -> None:
        """
        Constructor for the MakeGraph class.

        Args:
        - particle_list (list[Particle]): A list of Particle objects to be plotted.
        """
        self.particle_list: list[Particle] = particle_list
        
        self.fig, self.ax = plt.subplots()
        
        self._min_max_xy()
        self._set_xylim()
        
        self.data_length: int = len(self.particle_list[0].x_list)
    
    def _define_plot(self) -> None:
        """
        Internal method to define the plot for each particle.
        """
        for n, _ in enumerate(self.particle_list):
            self.ax.plot([], [], label=f"P{n}", alpha=0.6)
            
    def _min_max_xy(self) -> None:
        """
        Internal method to find the minimum and maximum x and y coordinates among all particles.
        """
        x_min_list: list[float] = []
        x_max_list: list[float] = []
        
        y_min_list: list[float] = []
        y_max_list: list[float] = []
        
        for particle in self.particle_list:
            x_min_list.append(min(particle.x_list))
            x_max_list.append(max(particle.x_list))

            y_min_list.append(min(particle.y_list))
            y_max_list.append(max(particle.y_list))
            
        self.min_x: float = min(x_min_list)
        self.max_x: float = max(x_max_list)
        
        self.min_y: float = min(y_min_list)
        self.max_y: float = max(y_max_list)
    
    def _set_xylim(self, x: Union[None, tuple[float, float]] = None, y: Union[None, tuple[float, float]] = None) -> None:
        """
        Internal method to set the x and y axis limits of the plot.

        Args:
        - x (Union[None, tuple[float, float]]): A tuple representing the desired x-axis limits.
        - y (Union[None, tuple[float, float]]): A tuple representing the desired y-axis limits.
        """
        self.ax.set_xlim(x[0], x[1]) if isinstance(x, tuple) else self.ax.set_xlim(self.min_x, self.max_x)
        self.ax.set_ylim(y[0], y[1]) if isinstance(y, tuple) else self.ax.set_ylim(self.min_y, self.max_y)

    def init_plot_function(self) -> None:
        """
        Initializes the plot and returns the axes object for further customization.
        """
        self._define_plot()
        return self.ax
    
    def animate_function(self, frame: int) -> None:
        """
        Updates the plot for each frame during animation.

        Args:
        - frame (int): The frame number for animation.
        """
        for n, particle in enumerate(self.particle_list):
            self.ax.lines[n].set_data(particle.x_list[:frame], particle.y_list[:frame])
        return self.ax

    def run(self) -> None:
        """
        Runs the animation by creating a FuncAnimation object and displaying the plot.
        """
        ani = FuncAnimation(
            self.fig,
            self.animate_function,
            frames=self.data_length,
            init_func=self.init_plot_function,
            blit=False,
            interval=1.5
        )
        
        plt.show()