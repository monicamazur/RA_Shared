import numpy as np
from scipy import optimize
import random
from App import GuesserTemplate, prm_mtrx_to_dict
from test import bounds_params


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
        # np.var(f) / np.mean(f)

        # here I am starting all parameter guesses at 0. Try to loop over different start values
        ntries = 10
        x0s = np.zeros((ntries, self.n_params()))

        # randomly generate 10 initial guesses between upper and low parameter bounds
        i = 0
        for shp, d_shp in bounds_params.items():
            for param, d_prm in d_shp.items():
                x0s[:, i] = random.sample(*bounds_params[shp][param], ntries)
                i += 1

        for i in range(x0s.shape[0]):
            best_fit_params = optimize.minimize(self, x0s[i,:], method=method)['x']

        self.params.clear()
        self.params.update(prm_mtrx_to_dict(best_fit_params, self.gen.params))
