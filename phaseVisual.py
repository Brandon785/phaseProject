
import pandas as pd
import matplotlib.pyplot as plt
import math
def main():
    data = pd.read_csv('pendulumT=0.0.csv')

    theta = data['theta']
    w = data['w']
    t = data['t']  # make sure your data has a 't' column
    K = 1
    T = 0.5
    theta1 = math.asin(T / K)
    data['theta_adjusted'] = data['theta'] - theta1

    plt.figure(figsize=(10, 6))
    plt.plot(t, theta, label='theta vs t')
    plt.plot(t, w, label='w vs t')

    plt.title('Pendulum Phase Profile')
    plt.xlabel('t')
    plt.legend()

    plt.show()

main()