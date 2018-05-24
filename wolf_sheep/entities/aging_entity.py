from wolf_sheep.entities.living_entity import LivingEntity


class AgingEntity(LivingEntity):
    """Class that offers basic aging functionality.

    Args:
        age (int, optional=0): entity age

    Attributes:
        age (int): entity age

    Static attributes:
        max_age (int): maximum age at which the entity will die
        min_min_reproduction_age (int): minimum age at which the entity can reproduce itself
    """

    max_age = 20
    min_reproduction_age = 1

    def __init__(self, age=0):
        super().__init__()
        self.age = age

    def _increment_age(self):
        """Template method used to increment age."""
        self.age += 1

    def _should_die(self):
        """Checks whether the entity should die according to its age."""
        return self.age >= self.max_age

    def _can_reproduce(self):
        """Checks whether the entity can reproduce according to its age."""
        return self.age > self.min_reproduction_age
