from wolf_sheep.entities.living_entity import LivingEntity


class EnergyConsumingEntity(LivingEntity):
    """Class that offers basic energy consuming functionality."""

    def __init__(self, energy=0):
        super().__init__()
        self.energy = energy

    def _decrement_energy(self):
        """Template method to decrement energy."""
        self.energy -= 1

    def _should_die(self):
        """Checks whether the entity should die according to its energy levels."""
        return self.energy < 0

    def _can_reproduce(self):
        """Checks whether the entity can reproduce according to its energy levels."""
        return not self._should_die()
