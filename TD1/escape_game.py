import numpy as np

# constants
states = 6
actions = 6
final_state = 5
reward = 100
no_reward = 0
gamma = 0.8 # futur reward

R = [
    [ -1, -1, -1, -1, 0, -1 ],
    [ -1, -1, -1, 0, -1, 100 ],
    [ -1, -1, -1, 0, -1, -1 ],
    [ -1, 0, 0, -1, 0, -1 ],
    [ 0, -1, -1, 0, -1, 100 ],
    [ -1, 0, -1, -1, 0, 100 ],
]

# 1. Initialize the Q-table
Q = [
    [ -1, -1, -1, -1, 0, -1 ],
    [ -1, -1, -1, 0, -1, 0 ],
    [ -1, -1, -1, 0, -1, -1 ],
    [ -1, 0, 0, -1, 0, -1 ],
    [ 0, -1, -1, 0, -1, 0 ],
    [ -1, 0, -1, -1, 0, 0 ],
]

# 2.a Using Bellman equation, compute the new value of Q(1,5)
# 2.b Update the Q-table accordingly
Q[1][5] = R[1][5] + gamma * np.max(Q[5,:])

# 3 
