# Bloch Sphere drawing

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def bloch_coordinates(state):
    alpha, beta = state
    x = 2 * np.real(np.conj(alpha) * beta)
    y = 2 * np.imag(np.conj(alpha) * beta)
    z = abs(alpha)**2 - abs(beta)**2
    return x, y, z

def plot_bloch(state, sphere_resolution=50, sphere_alpha=0.5):
    x, y, z = bloch_coordinates(state)

    # créer la figure et l'axe 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # tracer la sphère de Bloch en fil de fer
    step = np.pi/sphere_resolution
    u, v = np.mgrid[0:2*np.pi:step, 0:np.pi:step]
    xs = np.cos(u) * np.sin(v)
    ys = np.sin(u) * np.sin(v)
    zs = np.cos(v)
    ax.plot_wireframe(xs, ys, zs, color="lightgray", alpha=sphere_alpha)

    # tracer les axes X, Y, Z
    ax.quiver(0,0,0,1,0,0,color='r',length=1,label='X')
    ax.quiver(0,0,0,0,1,0,color='g',length=1,label='Y')
    ax.quiver(0,0,0,0,0,1,color='b',length=1,label='Z')

    # tracer le vecteur du qubit
    ax.scatter([x],[y],[z], color='k', s=100)

    # limites et labels
    ax.set_xlim([-1,1])
    ax.set_ylim([-1,1])
    ax.set_zlim([-1,1])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Bloch Sphere')

    plt.show()

def plot_bloch_trajectory(states):
    """
    states: list of successive qubit states
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # sphère
    u, v = np.mgrid[0:2*np.pi:100j, 0:np.pi:50j]
    xs = np.cos(u) * np.sin(v)
    ys = np.sin(u) * np.sin(v)
    zs = np.cos(v)
    ax.plot_wireframe(xs, ys, zs, color="lightgray", alpha=0.3)

    # axes
    ax.quiver(0,0,0,1,0,0,color='r',length=1)
    ax.quiver(0,0,0,0,1,0,color='g',length=1)
    ax.quiver(0,0,0,0,0,1,color='b',length=1)

    # extraire coordonnées des états successifs
    xs = []
    ys = []
    zs = []
    for s in states:
        x, y, z = bloch_coordinates(s)
        xs.append(x)
        ys.append(y)
        zs.append(z)

    # tracer la trajectoire
    ax.plot(xs, ys, zs, color='k', marker='o')

    ax.set_xlim([-1,1])
    ax.set_ylim([-1,1])
    ax.set_zlim([-1,1])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Qubit trajectory on the Bloch sphere')

    plt.show()


