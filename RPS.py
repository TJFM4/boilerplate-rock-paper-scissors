# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

from collections import deque, defaultdict
import random

# Hyperparameters
k = 4  # memory length (number of previous steps)
a = 1  # laplacian smoothing for non-zero probabilities
e = 0.04  # rate of randomness (avoids predictability)
pad = "pad"  # used to pad history data when insufficient plays have occured
opts = ["R", "P", "S"]

counters = {"R": "P", "P": "S", "S": "R"}

counts = defaultdict(
    lambda: {s: 0.0 for s in opts}
)  # each option begins at 0 counts, as defined in the dictionary
history = deque(maxlen=k)  # deque data format to easily append/remove data from memory


def current():
    if len(history) < k:
        return tuple(
            ([pad] * (k - len(history)) + list(history))
        )  # pad the memory if insufficient rounds have been played
    return tuple(history)


def update(prev_opp_move: str):  # ensures that the argument is a string
    if not prev_opp_move:
        return
    context = current()
    counts[context][prev_opp_move] += (
        1.0  # creates context specific dictionary to assess moves after a certain series of plays
    )
    history.append(prev_opp_move)  # add the previous opponent move to memory


def predict_opponent():
    context = current()
    table = counts[context]
    total = sum(table.values())
    denom = total + a * len(
        opts
    )  # denominator for the probability calculation of each move

    if denom == 0:
        dist = {
            s: 1.0 / len(opts) for s in opts
        }  # uniform distribution if there is no data
    else:
        dist = {
            s: (table[s] + a) / denom for s in opts
        }  # compute probabilities for all three possible moves

    pred = max(dist, key=dist.get)  # prediction is the maximum probability move
    return pred, dist


def player(prev_play, opponent_history=[]):
    update(prev_play)  # update knowledge of opponent play

    pred, _ = predict_opponent()  # predict opponent outcome

    if random.random() < e:  # accomodate some exploration to reduce predictability
        return random.choice(opts)
    return counters[pred]
