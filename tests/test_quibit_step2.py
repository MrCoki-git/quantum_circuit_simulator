from src.qubit import Qubit
import numpy as np

# Test 1 : Default state
q1 = Qubit()
print("Default state :", q1.state)  # expected : [1+0d, 0+0d]
# Test 2 : Personalised state
q2 = Qubit([3, 4])
print("Normalised state :", q2.state)

# Verification : sqrt(3² + 4²) = 5
# Thus normalisation → [0.6, 0.8]


