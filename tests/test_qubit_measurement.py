import numpy as np
from src.qubit import Qubit
from src.gates import H, X, Rx

# Create a qubit |0>
q = Qubit([1,0])

# Apply Hadamard → superposition
q.apply_gate(H)
print("Sate after H :", q.state)
print("Probabilities :", q.probabilities())

# Multiple measure to verify stats
counts = {0:0, 1:0}
for _ in range(1000):
    q = Qubit()
    q.apply_gate(H)
    result = q.measure()
    counts[result] += 1

print("Results after 1000 measurement with H :", counts)


# Test X :  |0> → |1>
q = Qubit([1,0])
q.apply_gate(X)
print("État après X :", q.state)
print("Probabilités :", q.probabilities())

# Test Rx(pi/2)
q = Qubit([1,0])
q.apply_gate(Rx(np.pi/2))
print("State after Rx(pi/2) :", q.state)
print("Probabilities :", q.probabilities())


