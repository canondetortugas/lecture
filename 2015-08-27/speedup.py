from pylab import *

import numpy as np

a = 0.1

p_range = np.array(range(1,129))

def E(p):
    return 1/(p*a + (1-a))
              
def S(p):
    return p*E(p)

if __name__=='__main__':
    ex = E(p_range)
    sx = S(p_range)
    plot(p_range, ex, label='efficiency')
    plot(p_range, sx, label='speedup')
    xlabel('number of cores')
    legend()
    show()
    
