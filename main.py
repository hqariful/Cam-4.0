import matplotlib.pyplot as plt
import numpy as np

global theta, r
# create angle variable from 0 to 360 degree
theta = np.linspace(0,360,360)
# similarly create radius variable with 0 unit
r = np.zeros(np.shape(theta))


def merger():
    new_angle = outStroke.angle
    r[:new_angle] = outStroke.outStroke(theta)
    prev_angle = new_angle
    new_angle += dwell
    r[prev_angle:new_angle] = max_disp
    prev_angle = new_angle
    new_angle += returnStroke.angle
    r[prev_angle:new_angle] = returnStroke.returnStroke(theta)
    return r

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

if __name__ == "__main__":
    from calculate.linear_tragectory import linear_tragectory as LT
    max_disp = 40
    outStroke = LT.Constant_Acceleration(60,max_disp)
    returnStroke = LT.Constant_Acceleration(120,max_disp)
    dwell = 30
    
    rF = 20 # Offset Distance
    rB = 50 # Base Circle
    plot_rad_cam = True
    r = merger()
    if plot_rad_cam == True : radial_plot() 
    else: disp_diag()
    # plt.savefig('new.png', dpi=200)
    plt.show()