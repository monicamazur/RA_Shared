import numpy as np
from scipy import optimize

from App import GuesserTemplate, prm_mtrx_to_dict

bounds_params = {
    'linear': {'a': (-10, 10), 'b': (-20, 20)},
    'exponential': {'a': (1, 10), 'b': (-1, 1)},
    'logistic': {'a': (-10, 10), 'b': (-10, 10), 'c': (-20, 20)},
    'inverse': {'a': (-40, 40), 'b': (0, 20)},
    'log': {'a': (-20, 20), 'b': (-20, 20)},
    'ocilacion': {'a': (-10, 10), 'b': (-5, 5), 'c': (0, np.pi)},
    'ocilacion_aten': {'a': (-1 / 2, 1 / 2), 'b': (-10, 10), 'c': (-2, 2), 'd': (0, np.pi)},
    'weight': {'b': (-10, 10), 'c': (-10, 10)},
}


class OptimiseGuesser(GuesserTemplate):

    def estimate(self, method=None):
        # guess the curve parameters and save them, in same structure as "params" from Generator, in self.params
        # IMPLEMENT Scipy Optimize
        # This cannot be done in a for-loop. You have to optimise all parameters at the same time! :)
        # I will implement this for a general case with fixed starting guesses as an example.
        # todo: implement this with different numbers of starting guesses to find out which one is best.
        # todo: (cont.) because the current example only uses 1 starting guess
        # Todo: **please understand very carefully here how I have used SciPy's function (without copying anything
        # todo: from SciPy internal entrails) and how each argument of the single call to a SciPy function corresponds
        # todo: to what the SciPy documentation asks for (function, matrix of arguments to optimise, and method).
        # todo: note that the current optimisation is *not* working! (as expected)
        # todo: 1) Write a function to normalise the input data, and try to set reasonable bounds for all
        # todo: (cont.) shp parameters for a normalised input data case
        # todo: 2) Then try implementing different starting points and different optimisation algorithms

        # This function will calculate the goodness of fit of a chosen parameter set p
        def f(p):
            return self._gof(params=prm_mtrx_to_dict(p, self.gen.params), measure='aic')

        # Normalize data

        # here I am starting all parameter guesses at 0. Try to loop over different start values
        ntries = 10
        x0s = np.zeros((ntries, self.n_params()))

        # randomly generate 10 initial guesses between upper and low parameter bounds
        bounds = {shp: d_shp for shp, d_shp in bounds_params.items() if shp in self.gen.params}
        i = 0
        for shp, d_shp in bounds.items():
            for param, d_prm in d_shp.items():
                x0s[:, i] = np.random.uniform(*bounds[shp][param], ntries)
                i += 1

        best_fit_params = None
        # check worst value for aic and set gof to that value
        # check aic equation
        # save x and fun
        for i in range(ntries):
            best_fit_params = optimize.minimize(f, x0s[i, :], method=method)['fun']

        self.params.clear()
        self.params.update(prm_mtrx_to_dict(best_fit_params, self.gen.params))
