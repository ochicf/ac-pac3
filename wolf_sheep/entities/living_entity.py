class LivingEntity(object):
    """Base case for a living entity. Provides template methods to be implemented by the supbclasses."""
    def __init__(self):
        super().__init__()

    def _eat(self):
        """Eat template method, to be implemented by the subclasses."""
        pass

    def _should_die(self):
        """Template method used to indicate whether entity should die, to be implemented by the subclasses."""
        pass

    def _die(self):
        """Die template method, to be implemented by the subclasses."""
        pass

    def _can_reproduce(self):
        """Template method used to indicate whether entity can reproduce, to be implemented by the subclasses."""
        pass

    def _reproduce(self):
        """Reproduce template method, to be implemented by the subclasses."""
        pass
