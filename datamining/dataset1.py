import matplotlib.pyplot as plt
import numpy as np

def true_function(x):
    '''doctest
    >>> true_function(0)
    0.0
    '''   
    y = np.sin(np.pi * x * 0.8)
    return y



if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
    fig = plt.figure()

    x = np.linspace(-np.pi, np.pi)
    
    plt.plot(x, true_function(x), color='r', ls='-', label='sin')

    plt.xlim(-1, 1)

    plt.axhline(0, ls='-', c='b', lw=0.5)
    plt.axvline(0, ls='-', c='b', lw=0.5)

    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    # plt.xticks(())

    # plt.show()

    # fig.savefig("ex1.1.png")



   