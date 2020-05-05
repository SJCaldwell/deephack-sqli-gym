import random
import gym import Env, logger
from gym import spaces
import numpy as np

class DeephackSqliEnv(Env):
    # do the thing

    def __init__(self, db):
        """
        db: The database to run sqli against
        """
        super(DeephackSqliEnv, self).__init__()

        self.db = db

        #initialize action space
        chars = list(string.ascii_lowercase + string.digits + "=.;_ '()|%")
        self.char_depth = len(chars)
        self.char_indices = dict((c, i) for i, c in enumerate(chars))
        self.indices_char = dict((i, c) for i, c in enumerate(chars))
        self.acton_space = spaces.Discrete(self.char_depth)



        self.action_space = []

    def step(self, action):
        # Execute step in the environment
        raise NotImplementedError()

    def reset(self):
        # Reset state of environment to initial state
        raise NotImplementedError()

    def render(self, mode='human', close=False):
        raise NotImplementedError()

