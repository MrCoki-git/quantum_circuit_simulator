# Gates Matrices

import numpy as np

def Rx(theta):
    """
    Rotation around the X-axis
    """
    return np.array([
        [np.cos(theta/2), -1j*np.sin(theta/2)],
        [-1j*np.sin(theta/2), np.cos(theta/2)]
    ], dtype=complex)


def Ry(theta):
    """
    Rotation around the Y-axis
    """
    return np.array([
        [np.cos(theta/2), -np.sin(theta/2)],
        [np.sin(theta/2),  np.cos(theta/2)]
    ], dtype=complex)


def Rz(theta):
    """
    Rotation around the Z-axis
    """
    return np.array([
        [np.exp(-1j*theta/2), 0],
        [0, np.exp(1j*theta/2)]
    ], dtype=complex)

# Identity gate
I = np.array([
    [1, 0],
    [0, 1]
], dtype=complex)

# Pauli-X = Rx(pi)
X = Rx(np.pi)

# Pauli-Y = Ry(pi)
Y = Ry(np.pi)

# Pauli-Z = Rz(pi)
Z = Rz(np.pi)

# Hadamard
H = (1 / np.sqrt(2)) * np.array([
    [1,  1],
    [1, -1]
], dtype=complex)


