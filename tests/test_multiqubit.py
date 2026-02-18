import numpy as np
from src.qubit import Qubit
from src.gates import H, X, Rx
from src.multi_qubit import *

# Create a qubit |0>
q1 = Qubit([1,0])

# Create a qubit |1>
q2 = Qubit([0,1])

q3 = Qubit([0, 1])

q4 = Qubit([1,0])

# Combine q1 and q2
mq = Qubits_to_MultiQubit([q1,q2,q3,q4])
print("Sate of m1=q1q2 : " + mq.human_readable_state())