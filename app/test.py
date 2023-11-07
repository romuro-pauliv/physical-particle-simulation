from classes.particle import Particle
from classes.force import Force


from animation.graph import MakeGraph


particle_list: list[Particle] = [
    Particle((5, 5), 1),
    Particle((5, -5), 1),
    Particle((-5, -5), 1),
    Particle((-5, 5), 1)
]

particle_list[0].define_init_velocity((0, 0))
particle_list[1].define_init_velocity((0, 0))
particle_list[2].define_init_velocity((0, 0))
particle_list[3].define_init_velocity((0, 0))


forces: dict[str, Force] = {}


frame_: int = 0

while frame_ < 1000:
    
    particles_numb: int = len(particle_list)
    
    for particle in range(0, particles_numb):
        for interations in range(particle, particles_numb):
            if particle != interations:
                forces[f"{particle}{interations}"] = Force(particle_list[particle].get_particle(), particle_list[interations].get_particle())
    
    for particle in range(0, particles_numb):
        for interations in range(particle, particles_numb):
            if particle != interations:
                particle_list[particle].define_force(forces[f"{particle}{interations}"].get_p1_force())
                particle_list[interations].define_force(forces[f"{particle}{interations}"].get_p2_force())
    
    for particle in particle_list:
        particle.update_frame(0.01)
    
    frame_ += 1



make_graph: MakeGraph = MakeGraph(particle_list)

make_graph._set_xylim((-10, 10), (-10, 10))
make_graph.run()