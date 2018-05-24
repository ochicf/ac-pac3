from mesa import Agent
from wolf_sheep.entities.energy_consuming_entity import EnergyConsumingEntity


class EnergyConsumingAgent(Agent, EnergyConsumingEntity):
    """Agent that consumes energy at every step.

    It extends `EnergyConsumingEntity` by adding `_is_energy_consuming_agent` template function, used to conditionally
    call all the energy related processes. This way, subclasses can choose when to apply the energy features.
    """

    def __init__(self, pos, model, energy):
        Agent.__init__(self, pos, model)
        EnergyConsumingEntity.__init__(self, energy)

    def step(self):
        """Decrements energy and eats if it is an energy consuming agent."""
        super().step()
        if self._is_energy_consuming_agent():
            self._decrement_energy()
            self._eat()

    def _is_energy_consuming_agent(self):
        """Template method that determines whether the entity is an energy consuming agent. Default to true."""
        return True

    def _should_die(self):
        """Add additional call to `self._is_energy_consuming_agent()`"""
        return self._is_energy_consuming_agent() and EnergyConsumingEntity._should_die(self)
