from App import GuesserTemplate

    import scipy

class OptimiseGuesser(GuesserTemplate):
    def estimate(self):
        # guess the curve parameters and save them, in same structure as "params" from Generator, in self.params
        raise NotImplementedError

        #create a dictionary for parameter limits with tuples

        lims_params = {
        'logistic': {'a':(,), 'b':(,), 'c':(,)},
        'exponential': {'a':(,),'b':(,)},
        }

        _methods_opt = {
            'Nelder-Mead': ,
            'Powell':
            'CG': ,
            'BFGS': ,
            'Newton-CG': ,
            'L-BFGS-B': ,
            'TNC': ,
            'COBYLA': ,
            'SLSQP': ,
            'trust-constr': ,
            'dogleg': ,
            'trust-exact':,
            'trust-krylov':,
        }


        #start the minimize function at different points
        _x_guess = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
        _y_guess = [1, 0.5, 2, 0.25, 4, 6, 2, 4, 1, 2]

        # or generate initial estimates by following the Tinamit example ?

        #optimize using all methods

        for x in _x_guess and for y in _y_guess

        opt = minimize(self,[x,y], bounds= [lims_params[p] for p in params], method='BFGS')
        #if the syntax in opt is correct, copy for theh other methods

        #save in same structure as "params" from Generator, in self.params
        return {p: {'val': opt.x[i]}} for i, p in enumerate(params)}



