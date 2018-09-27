from App import GuesserTemplate

import scipy as sp

class OptimiseGuesser(GuesserTemplate):
    def estimate(self):
        # guess the curve parameters and save them, in same structure as "params" from Generator, in self.params
        raise NotImplementedError