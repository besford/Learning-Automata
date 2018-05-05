import numpy as np
import scipy as sp

from abc import ABCMeta, abstractmethod

class LearningEnvironment(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def simulate(self):
        pass