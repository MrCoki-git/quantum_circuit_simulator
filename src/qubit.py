# Class Qubit + Operations

import numpy as np

class Qubit:
    def __init__(self, state=None):
        """
        state : liste or array [alpha,  beta]
        representing alpha|0> + beta|1>
        """
        if state is None:
            # Default state |0> = [1, 0]
            self.state = np.array([1, 0], dtype=complex)
        else:
            self.state = np.array(state, dtype=complex)
        
        # State normalisation
        self.normalise()

    def normalise(self):
        """ State vector normalisation """
        norm = np.linalg.norm(self.state)
        if norm == 0:
            raise ValueError("State Vector can't be null")
        self.state = self.state / norm
    
    def apply_gate(self, gate):
        """
        Apply a 2x2 quantum gate on the qubit.
        gate : numpy array 2x2
        """
        # matrix multiplication U|psi>
        self.state = gate @ self.state

        # renormalisation to avoid digital exesses
        self.normalise()

    def probabilities(self):
        """
        Returns an array with the probabilities of measuring |0> and |1>
        index 0 : probabilities of measuring |0>
        index 1 : probabilities of measuring |1>
        """
        alpha, beta = self.state
        return np.array([abs(alpha)**2, abs(beta)**2])
    
    def measure(self):
        """
        Simulates a qubit measurement.
        Returns 0 or 1, and updates the qubit state after measurement.
        """
        # calculate probabilities
        probs = self.probabilities()

        # random draw
        result = np.random.choice([0,1], p=probs)

        # projection : put the qubit into the measured state
        if result == 0:
            self.state = np.array([1,0], dtype=complex)
        else:
            self.state = np.array([0,1], dtype=complex)

        return result
    
    def human_readable_state(self) :
        res = str(self.state[0]) + "|0> + " + str(self.state[1]) + "|1>"
        return res

