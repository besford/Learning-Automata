import numpy as np
import scipy as sp

from abc import ABCMeta, abstractmethod

class LearningAutomata(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        '''Initialize states, memory, actions, penalties, etc'''
        pass
    
    @abstractmethod
    def env_resp(self, learning_env):
        '''Process response from environment'''
        pass
    
    @abstractmethod
    def next_state(self):
        '''Perform state translation in accordance to reward or penalty'''
        pass
    
    @abstractmethod
    def learn(self):
        '''Perform learning simulation for the Learning Automata'''
        pass

class TsetlinAutomata(LearningAutomata):
    def __init__(self, num_states, num_actions, penalties):
        self.memory = 2 * num_states
        self.states = []
        self.actions = np.zeros(num_actions)
        self.penalties = penalties
        self.current_state = int(self.memory / num_actions)

    def env_resp(self, learning_env):
        raise NotImplementedError('env_resp')
    
    def next_state(self, penalty):
        if penalty:
            self.update_on_penalty()
        elif not penalty:
            self.update_on_reward()

    def learn(self):
        raise NotImplementedError('learn')

    def update_on_penalty(self):
        if not self.is_boundary_state(self.current_state):
            self.decrement_current_state()
        else:
            self.cycle_current_state()

    def update_on_reward(self):
        if not self.is_optimal_state(self.current_state):
            self.increment_current_state()

    def decrement_current_state(self, amt=1):
        self.current_state -= amt
    
    def increment_current_state(self, amt=1):
        self.current_state += amt

    def cycle_current_state(self):
        if self.current_state == self.memory:
            self.current_state = self.memory / self.actions.size
        else:
            self.increment_current_state((self.memory / self.actions.size) % self.memory)

    def is_optimal_state(self, state):
        return state % (self.memory / self.actions.size) == 1
    
    def is_boundary_state(self, state):
        return state % (self.memory / self.actions.size) == 0

class KrinskyAutomata(TsetlinAutomata):
    def __init__(self, num_states, num_actions, penalties):
        TsetlinAutomata.__init__(self, num_states, num_actions, penalties)
    
    def update_on_reward(self):
        while not self.is_optimal_state(self.current_state):
            self.decrement_current_state()

class KrylovAutomata(TsetlinAutomata):
    def __init__(self, num_states, num_actions, penalties):
        TsetlinAutomata.__init__(self, num_states, num_actions, penalties)

    def next_state(self, penalty):
        if penalty:
            if sp.random.uniform(0, 1) >= 0.5:
                self.update_on_penalty()
            else:
                self.update_on_reward()
        elif not penalty:
            self.update_on_reward()
