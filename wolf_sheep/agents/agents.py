import random
from mesa import Agent
from wolf_sheep.agents.animal_agent import AnimalAgent


class Sheep(AnimalAgent):
    '''
    A sheep that walks around, reproduces (asexually) and gets eaten.

    The init is the same as the RandomWalker.
    '''

    def __init__(self, pos, model, moore, energy=0, age=0):
        super().__init__(pos, model, moore, energy, age)

    def _eat(self):
        """Eats grass.

        Note that no check for `model.grass` is performed since this method only will be called
        when `self._is_energy_consuming_agent()` returns true, and that check is already moved there
        """
        this_cell = self.model.grid.get_cell_list_contents([self.pos])
        grass_patch = [obj for obj in this_cell
                       if isinstance(obj, GrassPatch)][0]
        if grass_patch.fully_grown:
            self.energy += self.model.sheep_gain_from_food
            grass_patch.fully_grown = False

    def _is_energy_consuming_agent(self):
        """Sheeps only handle energy when model has the grass option activated."""
        return self.model.grass


class Wolf(AnimalAgent):
    '''
    A wolf that walks around, reproduces (asexually) and eats sheep.
    '''

    def __init__(self, pos, model, moore, energy=None, age=0):
        super().__init__(pos, model, moore, energy, age)

    def _eat(self):
        """Eats a sheep."""
        this_cell = self.model.grid.get_cell_list_contents([self.pos])
        sheep = [obj for obj in this_cell if isinstance(obj, Sheep)]
        if len(sheep) > 0:
            sheep_to_eat = random.choice(sheep)
            self.energy += self.model.wolf_gain_from_food

            # Kill the sheep
            self.model.grid._remove_agent(self.pos, sheep_to_eat)
            self.model.schedule.remove(sheep_to_eat)


class GrassPatch(Agent):
    '''
    A patch of grass that grows at a fixed rate and it is eaten by sheep
    '''

    def __init__(self, pos, model, fully_grown, countdown):
        '''
        Creates a new patch of grass

        Args:
            grown: (boolean) Whether the patch of grass is fully grown or not
            countdown: Time for the patch of grass to be fully grown again
        '''
        super().__init__(pos, model)
        self.fully_grown = fully_grown
        self.countdown = countdown

    def step(self):
        if not self.fully_grown:
            if self.countdown <= 0:
                # Set as fully grown
                self.fully_grown = True
                self.countdown = self.model.grass_regrowth_time
            else:
                self.countdown -= 1
