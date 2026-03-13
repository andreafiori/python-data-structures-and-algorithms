"""
Adapter Design Pattern | https://wikipedia.org/wiki/Adapter_pattern
"""
class Adapter:
    """ Adapter class to adapt an object to a new interface """

    def __init__(self, obj, **adapted_methods):
        self._obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        return getattr(self._obj, attr)
