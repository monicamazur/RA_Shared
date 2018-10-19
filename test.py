from App import Generator
from try_opt import OptimiseGuesser
from try_spotpy import SpotPyGuesser

params = {
    'logistic': {'a': -2.9, 'b': -0.9, 'c': 0},
    'exponential': {'a': -0.2, 'b': 0.8},
    'weight': {'b': -0.8, 'c': -5.8}
}

gen = Generator(params=params, n_steps=30)

print('Congratulations! You got past this line. Now go calibrate.')

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


print('Optimise\n==========')
_methods_opt = {
    'Nelder-Mead',
    'Powell',
    'CG',
    'BFGS',
    'Newton-CG',
    'L-BFGS-B',
    'TNC',
    'COBYLA',
    'SLSQP',
    'trust-constr',
    'dogleg',
    'trust-exact',
    'trust-krylov'
}
opt = OptimiseGuesser(gen)  # done: loop over all optimisation algorithms and find the best one
for m in _methods_opt:
    opt.estimate(method=m)
    print(opt.gof())
    print(opt.check_params())

print('SPOTPY\n==========')
sptpy = SpotPyGuesser(gen, method='abc')  # todo: loop over all spotpy methods and find the best one
sptpy.estimate()
print(sptpy.gof)
print(sptpy.check_params())
