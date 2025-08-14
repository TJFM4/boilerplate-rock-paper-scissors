# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

from collections import deque, defaultdict
import random

#Hyperparameters
k = 2                                           #memory length (number of previous steps)
a = 1                                           #laplacian smoothing for non-zero probabilities
e = 0.04                                        #rate of randomness (avoids predictability)
pad = "pad"                                     #used to pad history data when insufficient plays have occured

counters = {"R": "P", "P": "S", "S": "R"}

history = deque(maxlen=k)

def current():
    


def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    guess = "R"
    if len(opponent_history) > 2:
        guess = opponent_history[-2]

    return guess
