import matplotlib.pyplot as plt
import pandas as pd
import math
import numpy as np

# Determine the number of files
num_files = len(np.arange(0.0, 4.5, 0.5))

# Create a figure and a set of subplots
fig, axs = plt.subplots(num_files, 2, figsize=(10, 6*num_files))

# Loop over the range of files
for idx, i in enumerate(np.arange(0.0, 4.5, 0.5)):
    # Read the data file
    data = pd.read_csv(f'pendulumT={i}.csv')

    # Extract the columns
    theta = data['theta']
    w = data['w']
    t = data['t']
    torque = data['torque'][0]  # Assuming 'torque' is constant for each file

    # Adjust theta
    K = 1
    T = 0.5
    theta1 = math.asin(T / K)
    data['theta_adjusted'] = data['theta'] - theta1

    # Plot theta and w vs t
    axs[idx, 0].plot(t, theta, label=f'theta vs t, Torque={torque}')
    axs[idx, 1].plot(t, w, label=f'w vs t, Torque={torque}')

    # Set titles and labels
    axs[idx, 0].set_title(f'Theta vs Time for Torque={torque}')
    axs[idx, 0].set_xlabel('t')
    axs[idx, 0].legend()

    axs[idx, 1].set_title(f'Angular Velocity vs Time for Torque={torque}')
    axs[idx, 1].set_xlabel('t')
    axs[idx, 1].legend()

# Show the plot
plt.tight_layout()
plt.show()