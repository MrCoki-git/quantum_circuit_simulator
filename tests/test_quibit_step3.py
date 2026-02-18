from src.qubit import Qubit
from src.gates import X, H

# Test 1 : appliquer X sur |0>
q = Qubit()
q.apply_gate(X)
print("X|0> =", q.state)   # attendu environ [0, 1]

# Test 2 : appliquer H sur |0>
q = Qubit()
q.apply_gate(H)
print("H|0> =", q.state)   # attendu environ [0.707, 0.707]

