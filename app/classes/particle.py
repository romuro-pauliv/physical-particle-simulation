# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                                            app.classes.particle.py |
# |                                                                                             Author: Pauliv, Rômulo |
# |                                                                                          email: romulopauliv@bk.ru |
# |                                                                                                    encoding: UTF-8 |
# +--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
# |--------------------------------------------------------------------------------------------------------------------|


class Particle(object):
    def __init__(self, position: tuple[float, float], mass: float) -> None:
        self.x:     float = position[0]
        self.y:     float = position[1]
        
        self.mass:  float = mass
    
        self.x_velocity: float = 0
        self.y_velocity: float = 0

        self.x_force: float = 0
        self.y_force: float = 0
        
        self.x_list: list[float] = [self.x]
        self.y_list: list[float] = [self.y]
        
        self.define_none_force(False)
        
    def define_init_velocity(self, V: tuple[float, float]) -> None:
        self.x_velocity: float = V[0]
        self.y_velocity: float = V[1]
    
    def define_none_force(self, active: bool = False) -> None:
        self.none_force_button: bool = active
    
    def define_force(self, F: tuple[float, float]) -> None:
        if self.none_force_button == True:
            self.x_force: float = 0
            self.y_force: float = 0
            return None
        
        self.x_force: float = self.x_force + F[0]
        self.y_force: float = self.y_force + F[1]
    
    def _reset_force_var(self) -> None:
        self.x_force: float = 0
        self.y_force: float = 0
    
    def update_frame(self, time_: float) -> None:
        self.x_velocity: float = self.x_velocity + (self.x_force/self.mass)
        self.y_velocity: float = self.y_velocity + (self.y_force/self.mass)
        
        self.x: float = self.x + self.x_velocity*time_
        self.y: float = self.y + self.y_velocity*time_
    
        self.x_list.append(self.x)
        self.y_list.append(self.y)
        
        self._reset_force_var()
        
    def get_coordinates(self) -> tuple[list[float], list[float]]:
        return (self.x_list, self.y_list)
    
    def get_particle(self) -> tuple[float, float, float]:
        return self.x, self.y, self.mass