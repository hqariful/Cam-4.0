import matplotlib.pyplot as plt
import numpy as np
def disp_diag(theta, r):
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.plot(theta, r)
    ax.grid(True)
    plt.xlabel('theta')
    plt.ylabel('displacement')
    plt.show()

def radial_plot(theta, r, rB, rF):
    fig = plt.figure()
    rtheta = np.pi/180 * theta
    ax_r = fig.add_subplot(projection='polar')
    # below are the calculation for the radial plot and offset
    op_sid = (rB**2-rF**2)**0.5
    rad = (r**2 + 2*r*op_sid+rB**2)**0.5
    if rF==0: alpha=0 
    else: alpha = np.arctan((r+op_sid)/rF)
    if rF == 0 : phi = 0
    else: phi = np.arctan(op_sid/rF) # angle between op_sid and rF
    ax_r.plot(rtheta-np.arcsin(rF/rB)+(alpha-phi), rad)
    ax_r.grid(True)
    ax_r.set_theta_offset(np.pi/2)
    plt.show()