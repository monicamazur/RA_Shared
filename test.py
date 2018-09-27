from App import Generator
from try_opt import OptimiseGuesser
from try_spotpy import SpotPyGuesser

params = {
    'logistic': {},
    'exponential': {},
    'weight': {}
}  # todo: add actual parameter values

gen = Generator(params=params, n_steps=30)

print('Congratulations! You got past this line. Now go calibrate.')

print('Optimise\n==========')
opt = OptimiseGuesser(gen)
opt.estimate()
print(opt.gof)
print(opt.check_params())

print('SPOTPY\n==========')
sptpy = SpotPyGuesser(gen, method='abc')
sptpy.estimate()
print(sptpy.gof)
print(sptpy.check_params())
