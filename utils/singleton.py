from logging import getLogger


class Singleton:
    _instance = None
    lg = getLogger("daims")

    def __init__(self, cls):
        self._cls = cls

    def get_instance(self, *args, **kwargs):
        if self._instance:
            self.lg.debug(f"An instance of {self._cls} exists, ID is {id(self._instance)}")
            return self._instance
        else:
            self._instance = self._cls(*args, **kwargs)
            self.lg.debug(f"Getting new instance for {self._cls}, ID is {id(self._instance)}")
            return self._instance

    def __call__(self, *args, **kwargs):
        raise TypeError('Singletons must be accessed through `get_instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._cls)
