import numpy as np

def my_portfollo(x = np.array([10, 15]), \
    stock_matrics = np.array([[10.3, 7.5],[8.2, 7.9]])):
    return stock_matrics*x

if __name__ == "__main__":
    print my_portfollo(stock_matrics = np.array([[1.1, 2.2],[3.3, 4.4]]))