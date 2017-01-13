# counting the number of floors on the basis of windows coordinates
import numpy as np

def number_floors(wins):
    medium_h = 0
    for win in wins:
        medium_h += win[3]
    medium_h = medium_h/len(wins)
    floors = np.zeros(163)
    dw = wins[0][1]
    i = 0
    for win in wins:
        if abs(win[1] - dw) < medium_h / 2:
            floors[i] += 1
        else:
            dw = win[1]
            i += 1
            floors[i] += 1
    n_floors = np.count_nonzero(floors)
    return n_floors





