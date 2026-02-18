import numpy as np
from src.qubit import Qubit
from src.gates import H, Rx, Ry, Rz
from src.bloch import plot_bloch_trajectory

q = Qubit([1,0])
states = [q.state.copy()]

q.apply_gate(H)
states.append(q.state.copy())

q.apply_gate(Rx(np.pi/2))
states.append(q.state.copy())

q.apply_gate(Rz(np.pi/2))
states.append(q.state.copy())

plot_bloch_trajectory(states)
