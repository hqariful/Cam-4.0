import main
from calculate import linear_tragectory as LT
from grapher import disp_diag, radial_plot
max_disp = 40
dwell = 30
rF = 20 # Offset Distance
rB = 50 # Base Circle
outStroke = LT.Constant_Acceleration(60,max_disp)
returnStroke = LT.Constant_Acceleration(120,max_disp)
theta, r = main.main(outStroke,dwell,returnStroke, max_disp)
radial_plot(theta, r, rB, rF)