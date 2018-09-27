import matplotlib.pyplot as plt
import numpy as np


class Generator(object):
    def __init__(self, params, n_steps):
        shapes = list(params)
        shapes.remove('weight')

        self.params = params
        self.shapes = shapes
        self.curve = calc_curve(shapes, params, n_steps)


class GuesserTemplate():
    def __init__(self, generator):
        """

        :param generator:
        :type generator: Generator
        """
        # save reference to GenCurve object
        self.gen = generator

        self.params = None

    def estimate(self):
        raise NotImplementedError
        # guess the curve parameters and save them, in same structure as "params" from Generator, in self.params


    def gof(self, measure='aic'):
        if self.params is None:
            raise ValueError('You need to call estimate() first!')

        # returning a goodness of fit estimate for the fitted parameters
        gen = self.gen
        estim = calc_curve(gen.shapes, params=self.params, n_steps=len(gen.curve))
        truth = gen.curve
        n_params = 0
        for shp in self.params:
            n_params += len(self.params[shp])

        return calc_gof(n_params, estim, truth, measure=measure)

    def check_params(self):
        if self.params is None:
            raise ValueError('You need to call estimate() first!')
        true_params = self.gen.params
        estim_params = self.params

        check = {}
        for shp, d_true in true_params.items():
            check[shp] = {}
            for prm, true_val in d_true.items():
                estim_val = estim_params[shp][prm]
                check[shp][prm] = (estim_val - true_val)/true_val

        return check


def calc_gof(n_params, estim, truth, measure):

    if measure == 'aic':
        sse = np.sum((truth-estim)**2)
        n = len(truth)
        gof = 2*n_params - n*np.log(np.exp(2*np.pi*sse/n)+1)

    else:
        raise ValueError(measure)

    return gof


def calc_curve(shapes, params, n_steps):
    # calculate 2 shapes separately for n_steps (red and green)
    indiv_curves = [calc_one_curve(shp, params[shp], n_steps) for shp in shapes]

    # calculate transition weight for n_step (blue)
    w = NotImplemented  # todo : calculate the weight from params['weight']

    # return shape1 * weight + shape2*(1-weight)  # orange
    return indiv_curves[0] * w + indiv_curves[1] * (1-w)

def calc_one_curve(shp, prms, n_steps):
    x = np.arange(n_steps)
    if shp == 'linear':
        return linear(x=x, a=prms['a'], b=['b'])
    elif shp == 'exponential':
        raise NotImplementedError  # todo: implement all other basic shapes
    else:
        raise ValueError('Check your spelling for "{}"! :)'.format(shp))

# curve = self.plt.plot(np.linspace(0, 1, n_steps), wtd)
# plt.xlabel(‘Time (months)’)
# plt.ylabel(‘wtd (m)’)
# plt.title(“Plot”)


def linear(x, a, b):
    return a*x + b

def exponential(x, a, b):
    return a * (b ** x)

def logistic(x, a, b, c):
    return a / (1 + np.exp(-b * x + c))

def inverse(x, a, b):
    return a/(x + b)

def log(x, a, b):
    return a * np.log(x + b)

def ocilación(x, a, b, c):
    return a * np.sin(b * x + c)

def ocilación_aten(x, a, b, c, d):
    return np.exp(a * x) * b * np.sin(c * x + d)



