# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                                app.generator.newtonian_force_3D.py |
# |                                                                                             Author: Pauliv, Rômulo |
# |                                                                                          email: romulopauliv@bk.ru |
# |                                                                                                    encoding: UTF-8 |
# +--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from classes.particle.particle3D import Particle
from classes.forces.newtonian_force3D import Force
# |--------------------------------------------------------------------------------------------------------------------|


class Generator(object):
    def __init__(self, frames_: int, particle_list: list[Particle], update_frame: float) -> None:
        """
        Constructor for the Generator class.

        Args:
        - frames_ (int): The total number of frames to generate.
        - particle_list (list[Particle]): A list of Particle objects representing the particles in the system.
        - update_frame (float): The time increment for each frame update.
        """
        self.forces:            dict[str, Force]    = {}
        self.particle_list:     list[Particle]      = particle_list
        
        self.update_frame:  int     = update_frame
        self.qnt_particles: int     = len(particle_list)
        self.frames:        int     = frames_

    def _force_calculation(self) -> None:
        """
        Internal method to calculate forces between particles and store them in the `forces` dictionary.
        """
        for particle_number in range(0, self.qnt_particles):
            for interaction in range(particle_number, self.qnt_particles):
                if particle_number != interaction:
                    self.forces[f"{particle_number}{interaction}"] = Force(
                        self.particle_list[particle_number].get_particle(),
                        self.particle_list[interaction].get_particle()
                    )
    
    def _define_force(self) -> None:
        """
        Internal method to define forces for each particle based on the calculated forces.
        """
        for particle_number in range(0, self.qnt_particles):
            for interaction in range(particle_number, self.qnt_particles):
                if particle_number != interaction:
                    self.particle_list[particle_number].define_force(
                        self.forces[f"{particle_number}{interaction}"].get_p1_force()
                    )
                    self.particle_list[interaction].define_force(
                        self.forces[f"{particle_number}{interaction}"].get_p2_force()
                    )
    
    def _update_frame(self) -> None:
        """
        Internal method to update the state of each particle for the next frame.
        """
        for particle in self.particle_list:
            particle.update_frame(self.update_frame)
    
    
    def generate(self) -> None:
        """
        Generates and updates the system state over multiple frames.
        """
        frame: int = 0
        
        while frame < self.frames:
            
            self._force_calculation()
            self._define_force()
            self._update_frame()
            
            frame += 1
    
    def get_particle_list(self) -> list[Particle]:
        """
        Returns the list of Particle objects representing the particles in the system.

        Returns:
        - list[Particle]: A list of Particle objects.
        """
        return self.particle_list