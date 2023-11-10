# +--------------------------------------------------------------------------------------------------------------------|
# |                                                                                                    app.__main__.py |
# |                                                                                             Author: Pauliv, Rômulo |
# |                                                                                          email: romulopauliv@bk.ru |
# |                                                                                                    encoding: UTF-8 |
# +--------------------------------------------------------------------------------------------------------------------|

# | Imports |----------------------------------------------------------------------------------------------------------|
from classes.particle.particle3D import Particle

from generator.newtonian_force3D import Generator

from animation.graph_newtonian_force3D import MakeGraph

from random import uniform
# |--------------------------------------------------------------------------------------------------------------------|


if __name__ == "__main__":
    particle_list: list[Particle] = []
    
    
    for _ in range(0, 100):
        particle_list.append(Particle((uniform(-0.27, 0.27), uniform(-0.27, 0.27), uniform(-0.27, 0.27)), 1))
        # particle_list[-1].define_init_velocity((uniform(-100, 100), uniform(-100, 100), uniform(-100, 100)))

    generator: Generator = Generator(500, particle_list, 0.01)
    generator.generate()
    
    make_graph: MakeGraph = MakeGraph(generator.get_particle_list())
    make_graph._set_xylim((-40, 40), (-40, 40), (-40, 40))
    make_graph.run()
