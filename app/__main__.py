# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                                                    app.__main__.py |
# |                                                                                             Author: Pauliv, Rômulo |
# |                                                                                          email: romulopauliv@bk.ru |
# |                                                                                                    encoding: UTF-8 |
# +--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from classes.particle import Particle

from generator.newtonian_force import Generator

from animation.graph import MakeGraph

from random import uniform
# |--------------------------------------------------------------------------------------------------------------------|



particle_list: list[Particle] = []

particle_list.append(Particle((-100, 0), 50))
particle_list[0].define_init_velocity((60, 0))
particle_list[0].define_none_force(True)

for n in range(0, 50):
    particle_list.append(Particle((uniform(-100, 100), uniform(-100, 100)), 1))


generator: Generator = Generator(1000, particle_list, 0.01)
generator.generate()


make_graph: MakeGraph = MakeGraph(generator.get_particle_list())
make_graph._set_xylim((-100, 300), (-100, 100))
make_graph.run()