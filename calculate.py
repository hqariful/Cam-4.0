import matplotlib.pyplot as plt
import numpy as np

# Input Parameters
# type can be from i)Const Velocity ii)const acc iii)cyc or iv)shm

OS_info = {
    "type" : "const acc",
    "Ang" : 60
}
DW_Ang = 30
RS_info = {
    "type" : "const acc",
    "Ang" : 120
}

rB = 50 # Base Circle
F_Stroke = 40 # Follower Stroke
rF = 20 # Offset Distance
plot_rad_cam = True

def calculate():
    # create angle variable from 0 to 360 degree
    global theta, r
    theta = np.linspace(0,360,360)

    # similarly create radius variable with 0 unit
    r = np.zeros(np.shape(theta))

    # Extracting individual angle and shortening varibale names
    dOS = OS_info["Ang"] # Outstroke angle
    dRW = RS_info["Ang"] # Return Stroke angle
    dDw = DW_Ang # Dwell between Outstroke and Return Stroke

    r[dOS:dOS+dDw] = F_Stroke # Dwell (After Return Stroke) formula is same for every cam

    # Below formula are for linear constant velocity
    if OS_info["type"] == "Const Velocity":
        r[:dOS] = theta[:dOS]/dOS*F_Stroke
    if RS_info["type"] == "Const Velocity":
        r[dOS+dDw:dOS+dDw+dRW] = F_Stroke - theta[:dRW]/dRW*F_Stroke

    # Below formula are for simple harmonic motion
    if OS_info["type"] == "shm":
        r[:dOS] = F_Stroke/2-(F_Stroke/2)*np.cos(theta[:dOS]/dOS*np.pi)
    if RS_info["type"] == "shm":
        r[dOS+dDw:dOS+dDw+dRW] = F_Stroke/2 + (F_Stroke/2)*np.cos(theta[:dRW]/dRW*np.pi)

    # Below formula are for linear acceleration motion
    if OS_info["type"] == "const acc":
        m = 2*F_Stroke/dOS**2
        r[:int(dOS/2)] = m*theta[:int(dOS/2)]**2
        r[int(dOS/2):dOS] = F_Stroke - m*(theta[int(dOS/2):dOS]-dOS)**2
    if RS_info["type"] == "const acc":
        m = 2*F_Stroke/dRW**2
        r[dOS+dDw:dOS+dDw+int(dRW/2)] = F_Stroke-m*theta[:int(dRW/2)]**2
        r[dOS+dDw+int(dRW/2):dOS+dDw+dRW] = m*(theta[int(dRW/2):dRW]-dRW)**2

    # Below formula for cycloidal motion
    rG = F_Stroke/(2*np.pi) # Generating circle radius
    if OS_info["type"] == "cyc":
        r[:dOS] = theta[:dOS]/dOS*F_Stroke - rG*np.sin(theta[:dOS]/dOS*2*np.pi)
    if RS_info["type"] == "cyc":
        r[dOS+dDw:dOS+dDw+dRW] = F_Stroke - theta[:dRW]/dRW*F_Stroke + rG*np.sin(theta[:dRW]/dRW*2*np.pi)


def disp_diag():
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.plot(theta, r)
    ax.grid(True)
    plt.xlabel('theta')
    plt.ylabel('displacement')

def radial_plot():
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

def run():
    calculate()
    # saving the figure and showing displacement diagram or radial cam
    if plot_rad_cam == True : radial_plot() 
    else: disp_diag()
    plt.savefig('filename.png', dpi=200)
    plt.show()

if __name__ == "__main__":
    run()
