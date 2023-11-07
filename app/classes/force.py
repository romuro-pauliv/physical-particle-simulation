# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                                               app.classes.force.py |
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
        self.x1, self.y1, self.mass1 = particle_1
        self.x2, self.y2, self.mass2 = particle_2

        self.r: float = self._get_r()
        self.scalar_force: float = self._get_force_value()
        
        self.x_force: float = self._get_x_force()
        self.y_force: float = self._get_y_force()
        
    def _get_r(self) -> None:
        return ((self.x1 - self.x2)**2 + (self.y1 - self.y2)**2)**(1/2)
    
    def _get_force_value(self) -> None:
        return (self.mass1 * self.mass2)/(self.r)**2
    
    def _get_x_force(self) -> None:
        return self.scalar_force * (self.x2 - self.x1)
    
    def _get_y_force(self) -> None:
        return self.scalar_force * (self.y2 - self.y1)
    
    def get_p1_force(self) -> tuple[float, float]:
        return self.x_force, self.y_force
    
    def get_p2_force(self) -> tuple[float, float]:
        return -self.x_force, -self.y_force
    
    