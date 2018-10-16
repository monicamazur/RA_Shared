import numpy as np
from scipy import optimize
from pandas import Series
from sklearn.preprocessing import MinMaxScaler
from App import GuesserTemplate, prm_mtrx_to_dict


class OptimiseGuesser(GuesserTemplate):

    def estimate(self, method=None):
        # guess the curve parameters and save them, in same structure as "params" from Generator, in self.params

        # IMPLEMENT Scipy Optimize

        # This cannot be done in a for-loop. You have to optimise all parameters at the same time! :)

        # I will implement this for a general case with fixed starting guesses as an example.

        # todo: implement this with different numbers of starting guesses to find out which one is best.
        # todo: (cont.) because the current example only uses 1 starting guess

        # This function will calculate the goodness of fit of a chosen parameter set p
        def f(p):
            return self._gof(params=prm_mtrx_to_dict(p, self.gen.params), measure='aic')

        # here I am starting all parameter guesses at 0. Try to loop over different start values
        x0 = np.zeros(self.n_params())
        x0 = np.array([range([1,len(params[shp],1)])

        best_fit_params = optimize.minimize(self, x0, method=method)['x'])

        # Todo: **please understand very carefully here how I have used SciPy's function (without copying anything
        # todo: from SciPy internal entrails) and how each argument of the single call to a SciPy function corresponds
        # todo: to what the SciPy documentation asks for (function, matrix of arguments to optimise, and method).

        self.params.clear()
        self.params.update(prm_mtrx_to_dict(best_fit_params, self.gen.params))

        # todo: note that the current optimisation is *not* working! (as expected)
        # todo: 1) Write a function to normalise the input data, and try to set reasonable bounds for all
        # todo: (cont.) shp parameters for a normalised input data case
        # todo: 2) Then try implementing different starting points and different optimisation algorithms

        values = self.series.values
        values = self.series.reshape((len(values),1))

        # train the normalization
        scaler = MinMaxScaler(feature_rangeg=(0,1))
        scaler = scaler.fit(values)
        normalized = scaler.transform(values)

        lims_params = {
                'logistic': {'a': (-10,10), 'b': (-10,10), 'c': (0,-20)},
                'exponential': {'a': (1, 10), 'b': (-1, 1)},


        best_fit_params = optimize.minimize(self, x0, method=method)['x']
