# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                          app.animation.graph_newtonian_force_3D.py |
# |                                                                                             Author: Pauliv, Rômulo |
# |                                                                                          email: romulopauliv@bk.ru |
# |                                                                                                    encoding: UTF-8 |
# +--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from classes.particle.particle3D import Particle

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
        
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(projection="3d")
        
        self._min_max_xy()
        self._set_xylim()
        
        self.data_length: int = len(self.particle_list[0].x_list)
    
    def _define_plot(self) -> None:
        """
        Internal method to define the plot for each particle.
        """
        for n, _ in enumerate(self.particle_list):
            if n == 0:
                self.ax.plot([], [], [], color="red")
            if n == 1:
                self.ax.plot([], [], [], color="blue")
            if n == 2:
                self.ax.plot([], [], [], color="green")
            self.ax.plot([], [], [], alpha=0.3, color="gray")
            
    def _min_max_xy(self) -> None:
        """
        Internal method to find the minimum and maximum x and y coordinates among all particles.
        """
        x_min_list: list[float] = []
        x_max_list: list[float] = []
        
        y_min_list: list[float] = []
        y_max_list: list[float] = []
        
        z_min_list: list[float] = []
        z_max_list: list[float] = []
        
        for particle in self.particle_list:
            x_min_list.append(min(particle.x_list))
            x_max_list.append(max(particle.x_list))

            y_min_list.append(min(particle.y_list))
            y_max_list.append(max(particle.y_list))
            
            z_min_list.append(min(particle.z_list))
            z_max_list.append(max(particle.z_list))
            
        self.min_x: float = min(x_min_list)
        self.max_x: float = max(x_max_list)
        
        self.min_y: float = min(y_min_list)
        self.max_y: float = max(y_max_list)
        
        self.min_z: float = min(y_min_list)
        self.max_z: float = max(y_max_list)
    
    def _set_xylim(self, x: Union[None, tuple[float, float]] = None,
                         y: Union[None, tuple[float, float]] = None,
                         z: Union[None, tuple[float, float]] = None) -> None:
        """
        Internal method to set the x and y axis limits of the plot.

        Args:
        - x (Union[None, tuple[float, float]]): A tuple representing the desired x-axis limits.
        - y (Union[None, tuple[float, float]]): A tuple representing the desired y-axis limits.
        """
        self.ax.set(xlim3d=(x[0], x[1]), xlabel="X") if isinstance(x, tuple) else self.ax.set(xlim3d=(self.min_x, self.max_x), xlabel="X")
        self.ax.set(ylim3d=(y[0], y[1]), ylabel="X") if isinstance(y, tuple) else self.ax.set(ylim3d=(self.min_y, self.max_y), ylabel="Y")
        self.ax.set(zlim3d=(z[0], z[1]), zlabel="Z") if isinstance(z, tuple) else self.ax.set(zlim3d=(self.min_z, self.max_z), zlabel="Z")
        
        
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
           self.ax.lines[n].set_3d_properties(particle.z_list[:frame])
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