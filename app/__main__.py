# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                                                    app.__main__.py |
# |                                                                                             Author: Pauliv, Rômulo |
# |                                                                                          email: romulopauliv@bk.ru |
# |                                                                                                    encoding: UTF-8 |
# +--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from classes.particle.particle2D import Particle

from generator.newtonian_force2D import Generator

from animation.graph import MakeGraph

from random import uniform
# |--------------------------------------------------------------------------------------------------------------------|


particle_list: list[Particle] = []

for _ in range(0, 10):
    particle_list.append(Particle((uniform(-10, 10), uniform(-10, 10)), 1))

generator: Generator = Generator(1000, particle_list, 0.01)
generator.generate()


make_graph: MakeGraph = MakeGraph(generator.get_particle_list())
make_graph._set_xylim((-20, 20), (-20, 20))
make_graph.run()