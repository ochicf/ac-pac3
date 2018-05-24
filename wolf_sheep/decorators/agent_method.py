def agent_method_print(action=None, verbose_only=True, when='before'):
    """Decorates an agent method to easily print information about its call.

    Args:
        action (str, optional): name of the action to print, defaults to the decorated method's name
        verbose_only (bool, optional): whether to print the message only when model.verbose == True or always
        when ('before'|'after'|'both'): when to print the message respect to the method call
    """

    def agent_method_print_decorator(func):
        _action = func.__name__ if action is None else action

        def _print(self, *args):
            if (verbose_only and self.model.verbose) or not verbose_only:
                print(type(self).__name__ + '@' + ','.join(map(str, self.pos)) + ' ' + str(_action) + ': energy=' +
                      str(self.energy) + ' | age=' + str(self.age))

        def agent_method_print_wrapper(self, *args):
            if when == 'before' or when == 'both':
                _print(self, *args)
            value = func(self, *args)
            if when == 'after' or when == 'both':
                _print(self, *args)
            return value

        return agent_method_print_wrapper

    return agent_method_print_decorator

