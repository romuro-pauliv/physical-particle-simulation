# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                            app.classes.forces.newtonian_force2D.py |
# |                                                                                             Author: Pauliv, Rômulo |
# |                                                                                          email: romulopauliv@bk.ru |
# |                                                                                                    encoding: UTF-8 |
# +--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
# |--------------------------------------------------------------------------------------------------------------------|

class ForceType:
    particle = tuple[float, float, float]


class Force(object):
    def __init__(self, particle_1: ForceType.particle, particle_2: ForceType.particle) -> None:
        """
        Constructor for the Force class.

        Args:
        - particle_1 (tuple[float, float, float]): A tuple representing the first particle's (x, y, mass).
        - particle_2 (tuple[float, float, float]): A tuple representing the second particle's (x, y, mass).
        """
        self.x1, self.y1, self.mass1 = particle_1
        self.x2, self.y2, self.mass2 = particle_2

        self.r: float = self._get_r()
        self.scalar_force: float = self._get_force_value()
        
        self.x_force: float = self._get_x_force()
        self.y_force: float = self._get_y_force()
        
    def _get_r(self) -> None:
        """
        Calculates the distance (r) between the two particles and assigns it to the `r` attribute.
        """
        return ((self.x1 - self.x2)**2 + (self.y1 - self.y2)**2)**(1/2)
    
    def _get_force_value(self) -> None:
        """
        Calculates the magnitude of the force between the two particles and assigns it to the `scalar_force` attribute.
        """
        return (self.mass1 * self.mass2)/(self.r)**2
    
    def _get_x_force(self) -> None:
        """
        Calculates the force in the x-direction and assigns it to the `x_force` attribute.
        """
        return self.scalar_force * (self.x2 - self.x1)
    
    def _get_y_force(self) -> None:
        """
        Calculates the force in the y-direction and assigns it to the `y_force` attribute.
        """
        return self.scalar_force * (self.y2 - self.y1)
    
    def get_p1_force(self) -> tuple[float, float]:
        """
        Returns the force components acting on the first particle as a tuple (x_force, y_force).

        Returns:
        - tuple[float, float]: A tuple representing the force components (x_force, y_force) acting on the first particle.
        """
        return self.x_force, self.y_force
    
    def get_p2_force(self) -> tuple[float, float]:
        """
        Returns the force components acting on the second particle as a tuple (-x_force, -y_force).

        Returns:
        - tuple[float, float]: A tuple representing the force components (-x_force, -y_force) acting on the second
        particle.
        """
        return -self.x_force, -self.y_force
    
    