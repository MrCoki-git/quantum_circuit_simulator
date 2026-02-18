import numpy as np
from src.qubit import Qubit
from src.gates import H, Rx, Rz
from src.bloch import plot_bloch

q = Qubit([1,0])   # state : |0>
plot_bloch(q.state)  # point at North Pole of Bloch Sphere

q.apply_gate(H)
plot_bloch(q.state)  # point on the equatorial plane X-Y -> pole correspondant à |+>

q.apply_gate(Rx(np.pi/2))
plot_bloch(q.state)  # rotation around X

