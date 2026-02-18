# Class MultiQubit

import numpy as np
from functools import reduce
from operator import matmul
from . import gates as G  # relative import inside package
from src.qubit import Qubit

def kron_n(op_list):
    """Tensor product of list of 2x2 or larger matrices (left-to-right)."""
    return reduce(np.kron, op_list)

def Qubits_to_MultiQubit(qubits_list):
    """ Converting a list of qubits into a multi-qubit (to enable entanglement, for example) """
    state = np.array([], dtype=complex)
    for i in range(0, 2**len(qubits_list) ):
        coeff_of_state = 1
        str_of_state = str(bin(i))
        
        while(len(str_of_state)<len(qubits_list)+2):
            str_of_state = str_of_state[0:2] + "0" + str_of_state[2:]

        for j in range(len(str_of_state)-2):
            if(str_of_state[j+2] == "0"):
                coeff_of_state *= (qubits_list[j].state)[0]
            elif(str_of_state[j+2] == "1"):
                coeff_of_state *= (qubits_list[j].state)[1]
        state = np.append(state, coeff_of_state)

    return MultiQubit(len(qubits_list), state)

class MultiQubit:
    """
    State-vector simulator for n qubits (dense).
    state is a complex vector of length 2**n, in computational basis order.
    """

    def __init__(self, n:int, state=None ):
        self.n = int(n)
        self.dim = 2**self.n
        if state is None:
            self.state = np.zeros(self.dim, dtype=complex)
            self.state[0] = 1.0 + 0j  # |00...0>
        else:
            self.state = state
        self.normalise()

    def reset(self):
        self.state[:] = 0
        self.state[0] = 1.0 + 0j

    def normalise(self):
        """ State vector normalisation """
        norm = np.linalg.norm(self.state)
        if norm == 0:
            raise ValueError("State Vector can't be null")
        self.state = self.state / norm

    def probabilities(self):
        return np.abs(self.state)**2

    def apply_full_gate(self, U):
        """Apply a full 2^n x 2^n unitary U to the state."""
        if U.shape != (self.dim, self.dim):
            raise ValueError("Gate dimension mismatch.")
        self.state = U @ self.state
        # numerical renormalise
        self.normalise()

    def single_qubit_gate(self, gate, target):
        """
        Apply single-qubit gate (2x2 matrix) on qubit 'target' (0 = least significant / rightmost).
        Convention: ordering is qubit n-1 ... q1 q0, with q0 the least significant bit.
        """
        ops = []
        for i in range(self.n-1, -1, -1):  # build left-to-right for kronecker
            if i == target:
                ops.append(gate)
            else:
                ops.append(np.eye(2, dtype=complex))
        U = kron_n(ops)
        self.apply_full_gate(U)

    def controlled_gate(self, gate, control, target):
        """
        Apply controlled-single-qubit 'gate' with single control qubit.
        U = P0_control ⊗ I_rest + P1_control ⊗ (gate_on_target ⊗ I_rest)
        Implementation constructs full operator (dense).
        """
        P0 = np.array([[1,0],[0,0]], dtype=complex)
        P1 = np.array([[0,0],[0,1]], dtype=complex)

        # build operator for projector 0 branch: control=0 -> identity on target
        ops0 = []
        ops1 = []
        for i in range(self.n-1, -1, -1):
            if i == control:
                ops0.append(P0)
                ops1.append(P1)
            elif i == target:
                ops0.append(np.eye(2, dtype=complex))
                ops1.append(gate)
            else:
                ops0.append(np.eye(2, dtype=complex))
                ops1.append(np.eye(2, dtype=complex))

        U0 = kron_n(ops0)
        U1 = kron_n(ops1)
        U = U0 + U1
        self.apply_full_gate(U)

    def measure(self):
        """
        Perform projective measurement in computational basis.
        Returns integer in [0, 2^n - 1] and collapses state to that basis state.
        """
        probs = self.probabilities()
        idx = np.random.choice(self.dim, p=probs)
        new_state = np.zeros_like(self.state)
        new_state[idx] = 1.0 + 0j
        self.state = new_state
        return idx

    def measure_counts(self, shots=1024):
        """Return dictionary of counts for repeated measurements (non-destructive: resets each shot)."""
        counts = {}
        for _ in range(shots):
            s = self.state.copy()
            probs = np.abs(s)**2
            idx = np.random.choice(self.dim, p=probs)
            counts[idx] = counts.get(idx, 0) + 1
        return counts

    def set_state_from_amplitudes(self, amplitudes):
        a = np.array(amplitudes, dtype=complex)
        if a.size != self.dim:
            raise ValueError("Amplitude vector size mismatch.")
        self.state = a
        self.normalise()

    def human_readable_state(self) :
        res = ""
        for i in range(self.dim -1):
            temp = ""
            for j in range(4-len(str(bin(i)[2:]))) :
                temp+="0"
            res += str(self.state[i]) + "|" + temp + str(bin(i)[2:]) + "> + "
        res += str(self.state[self.dim-1]) + "|" + str(bin(self.dim-1)[2:]) + ">"
        return res
