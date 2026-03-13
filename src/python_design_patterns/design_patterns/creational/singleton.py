"""
Singleton creational design pattern | https://wikipedia.org/wiki/Singleton_pattern
"""
class Singleton:
    """ Singleton implementation """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
