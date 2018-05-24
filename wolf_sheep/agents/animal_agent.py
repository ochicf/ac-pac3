from wolf_sheep.agents.aging_agent import AgingAgent
from wolf_sheep.agents.energy_consuming_agent import EnergyConsumingAgent
from wolf_sheep.random_walk import RandomWalker
from wolf_sheep.decorators.agent_method import agent_method_print


class AnimalAgent(AgingAgent, EnergyConsumingAgent, RandomWalker):
    """
    Animal that walks around, reproduces (asexually), ages and gets eaten.
    """

    def __init__(self, pos, model, moore, energy=None, age=0):
        AgingAgent.__init__(self, pos, model, age)
        EnergyConsumingAgent.__init__(self, pos, model, energy)
        RandomWalker.__init__(self, pos, model, moore)

    def step(self):
        """
        A model step. Ages, moves, eats, then dies or reproduces.
        """
        AgingAgent.step(self)
        self.random_move()
        EnergyConsumingAgent.step(self)

        if self._should_die():
            self._die()
        elif self._can_reproduce():
            self._reproduce()

    def _should_die(self):
        """Checks whether the animal should die according to its age and energy levels."""
        return AgingAgent._should_die(self) \
            or EnergyConsumingAgent._should_die(self)

    @agent_method_print()
    def _die(self):
        """Implements how an animal dies. Removes it from the model."""
        self.model.grid._remove_agent(self.pos, self)
        self.model.schedule.remove(self)

    def _can_reproduce(self):
        """Checks whether the animal can reproduce according to its age and energy levels."""
        return AgingAgent._can_reproduce(self) \
            and EnergyConsumingAgent._can_reproduce(self) \
            and self.model.can_reproduce(self)

    @agent_method_print(action='_reproduce.before', when='before')
    @agent_method_print(action='_reproduce.after', when='after')
    def _reproduce(self):
        """Implements animal reproduction. Creates a new agent of the same type and gives it half the energy."""
        if self._is_energy_consuming_agent():
            self.energy /= 2

        child = type(self)(self.pos, self.model, self.moore, self.energy)
        self.model.grid.place_agent(child, self.pos)
        self.model.schedule.add(child)
