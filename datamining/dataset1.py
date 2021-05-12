import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def true_function(x):
    '''doctest
    >>> true_function(0)
    0.0
    '''   
    y = np.sin(np.pi * x * 0.8)
    return y


# -1以上1未満の観測点をランダムに20個用意
observation_points = (1-(-1)) * np.random.rand(20) + (-1) 

# 用意した観測点とそれに対応する真値をDataFrame型で保存
columns2 = ["観測点", "真値"]
df = pd.DataFrame(columns=columns2)
for i in observation_points:
    df1 = pd.DataFrame(data = [[i, true_function(i)]], columns = columns2)
    df = df.append(df1, ignore_index = True)

print(df)




if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
    fig = plt.figure()
    x = np.linspace(-np.pi, np.pi)
    
    
    plt.plot(x, true_function(x), color='r', ls='-', label='sin')

    plt.scatter(df["観測点"], df["真値"], label='サンプル集合')


    # x,y軸を描写
    plt.xlim(-1, 1)
    plt.axhline(0, ls='-', c='b', lw=0.5)
    plt.axvline(0, ls='-', c='b', lw=0.5)

    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    # plt.xticks(())
    
    plt.show()

    # fig.savefig("ex1.1.png")
    fig.savefig("ex1.2.png")



   