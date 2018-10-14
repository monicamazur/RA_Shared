from App import GuesserTemplate
import spotpy

class SpotPyGuesser(GuesserTemplate):
    def __init__(self, generator, method='mle'):
        self.method = method
        super().__init__(generator)

    def estimate(self):
        # guess the curve parameters and save them, in same structure as "params" from Generator, in self.params
        # access the spotpy method with self.method
        raise NotImplementedError

        self.params = [spotpy.parameter.list('x',[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]),
                       spotpy.parameter.list('y', [1, 0.5, 2, 0.25, 4, 6, 2, 4, 1, 2])]

        def parameters(self):
            return.spotpy.parameter.generate(self.params)

        def simulation(self, vector):
            x = np.array(vector)
            simulations = [sum(100.0 * (x[1:] - x[:-1] ** 2.0) ** 2.0 + (1 - x[:-1]) ** 2.0)]
            return simulations

        def evaluation(self):
            observations = [0]
            return observations

        def objectivefunction(self, simulation, evaluation):
            objectivefunction = -spotpy.objectivefunctions.rmse(evaluation, simulation)
            return objectivefunction

        _algs_spotpy = {
        'fast': spotpy.algorithms.fast,
        'dream': spotpy.algorithms.dream,
        'mc': spotpy.algorithms.mc,
        'mcmc': spotpy.algorithms.mcmc,
        'mle': spotpy.algorithms.mle,
        'lhs': spotpy.algorithms.lhs,
        'sa': spotpy.algorithms.sa,
        'sceua': spotpy.algorithms.sceua,
        'rope': spotpy.algorithms.rope,
        'abc': spotpy.algorithms.abc,
        'fscabc': spotpy.algorithms.fscabc,

        }

            if method in _algs_spotpy:

            sampler = _algs_spotpy[method](self, dbname='Iterator_example',
                                           dbformat='csv')  # Parameter lists can be sampled with MC

             sampler.sample(10)  # Choose equally (or less) repetitions as you have parameters in your List

