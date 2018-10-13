from App import GuesserTemplate

class SpotPyGuesser(GuesserTemplate):
    def __init__(self, generator, method='mle'):
        self.method = method
        super().__init__(generator)

    def estimate(self, method=None):
        # guess the curve parameters and save them, in same structure as "params" from Generator, in self.params
        # access the spotpy method with self.method

        if method is None:
            method = 'mle'

        raise NotImplementedError
