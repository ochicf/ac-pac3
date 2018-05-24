from mesa import Agent
from wolf_sheep.entities.aging_entity import AgingEntity


class AgingAgent(Agent, AgingEntity):
    """Agent that ages at every step."""

    def __init__(self, pos, model, age=0):
        Agent.__init__(self, pos, model)
        AgingEntity.__init__(self, age)

    def step(self):
        super().step()
        self._increment_age()
