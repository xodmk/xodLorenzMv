###############################################################################
#//////////////////////////////////////////////////////////////////////////////
#header begin------------------------------------------------------------------
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
###############################################################################

#__::((xodLorenzMv.py))::__

#Solve the Lorenz ODE system, and create animation.


###############################################################################
#//////////////////////////////////////////////////////////////////////////////
#header end--------------------------------------------------------------------
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
###############################################################################

import numpy as np
from scipy import integrate

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import cnames
from matplotlib import animation

###############################################################################
#//////////////////////////////////////////////////////////////////////////////
#function definitions begin----------------------------------------------------
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
###############################################################################


#//////////////////////////////////////////////////////////////////////////////
#lorenz_dt function begin------------------------------------------------------
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def lorenz_dt((x, y, z), to, sigma=10., beta=8./3, rho=28.0):
    """compute the time-derivative of a Lorenz system"""
    return [sigma*(y - x), x*(rho - z) - y, x*y - beta*z]

#//////////////////////////////////////////////////////////////////////////////
#lorenz_dt function end--------------------------------------------------------
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


###############################################################################
#//////////////////////////////////////////////////////////////////////////////
#function definitions end------------------------------------------------------
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
###############################################################################


###############################################################################
#//////////////////////////////////////////////////////////////////////////////
#main--------------------------------------------------------------------------
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
###############################################################################


nTrajectories = 33


# choose random starting points, uniformly distributed from -15 to 15
np.random.seed(1)
x0 = -15 + 30*np.random.random((nTrajectories, 3))

# solove for the trajectories
# set to 2x #frames to match video cycle
t = np.linspace(0, 4, 1554)
x_t = np.asarray([integrate.odeint(lorenz_dt, x0i, t) for x0i in x0])


###############################################################################
#//////////////////////////////////////////////////////////////////////////////
#Main end----------------------------------------------------------------------
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
###############################################################################



###############################################################################
#//////////////////////////////////////////////////////////////////////////////
#VideoGen begin----------------------------------------------------------------
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
###############################################################################


#//////////////////////////////////////////////////////////////////////////////
#setup & definitions begin-----------------------------------------------------
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#Create dictionary of math text examples:
odmk_pyLaTeX = {
    0: r"$W^{3\beta}_{\delta_1 \rho_1 \sigma_2} = "
    r"U^{3\beta}_{\delta_1 \rho_1} + \frac{1}{8 \pi 2} "
    r"\int^{\alpha_2}_{\alpha_2} d \alpha^\prime_2 \left[\frac{ "
    r"U^{2\beta}_{\delta_1 \rho_1} - \alpha^\prime_2U^{1\beta}_"
    r"{\rho_1 \sigma_2} }{U^{0\beta}_{\rho_1 \sigma_2}}\right]$",

    1: r"$f(t) = e^{-t}*cos(2\pi t)$",

    2: r"$g(x) = A*exp \left ( -\frac{(x-\mu )^{2}}{2*\sigma ^{2}} \right ) +d$",

    3: r"$g(x) = A*exp \left ( -\frac{(x-\mu )^{2}}{2*\sigma ^{2}} \right ) +d$",

    4: r"$\frac{3}{4},\ \binom{3}{4},\ \stackrel{3}{4},\ "
    r"\left(\frac{5 - \frac{1}{x}}{4}\right),\ \ldots$",

    5: r"$\sqrt{2},\ \sqrt[3]{x},\ \ldots$",

    6: r"$\mathrm{Roman}\ , \ \mathit{Italic}\ , \ \mathtt{Typewriter} \ "
    r"\mathrm{or}\ \mathcal{CALLIGRAPHY}$",

    7: r"$\acute a,\ \bar a,\ \breve a,\ \dot a,\ \ddot a, \ \grave a, \ "
    r"\hat a,\ \tilde a,\ \vec a,\ \widehat{xyz},\ \widetilde{xyz},\ "
    r"\ldots$",

    8: r"$\alpha,\ \beta,\ \chi,\ \delta,\ \lambda,\ \mu,\ "
    r"\Delta,\ \Gamma,\ \Omega,\ \Phi,\ \Pi,\ \Upsilon,\ \nabla,\ "
    r"\aleph,\ \beth,\ \daleth,\ \gimel,\ \ldots$",

    9: r"$\coprod,\ \int,\ \oint,\ \prod,\ \sum,\ "
    r"\log,\ \sin,\ \approx,\ \oplus,\ \star,\ \varpropto,\ "
    r"\infty,\ \partial,\ \Re,\ \leftrightsquigarrow, \ \ldots$"}

#define colors
#http://www.rapidtables.com/web/color/RGB_Color.htm
mplot_black = (0./255., 0./255., 0./255.)
mplot_white = (255./255., 255./255., 255./255.)
mplot_red = (255./255., 0./255., 0./255.)
mplot_orange = (255/255., 165/255., 0./255.)
mplot_darkorange = (255/255., 140/255., 0./255.)
mplot_orangered = (255/255., 69/255., 0./255.)
mplot_yellow = (255./255., 255./255., 0./255.)
mplot_lime = (0./255., 255./255., 0./255.)
mplot_green = (0./255., 128./255., 0./255.)
mplot_darkgreen = (0./255., 100./255., 0./255.)
mplot_cyan = (0./255., 255./255., 255./255.)
mplot_blue = (0./255., 0./255., 255./255.)
mplot_midnightblue = (25./255., 25./255., 112./255.)
mplot_magenta = (255./255., 0./255., 255./255.)
mplot_grey = (128./255., 128./255., 128./255.)
mplot_darkgrey = (64./255., 64./255., 64./255.)
mplot_darkdarkgrey = (32./255., 32./255., 32./255.)
mplot_silver = (192./255., 192./255., 192./255.)
mplot_purple = (128./255., 0./255., 128./255.)
mplot_maroon = (128./255., 0./255., 0./255.)
mplot_olive = (128./255., 128./255., 0./255.)
mplot_teal = (0./255., 128./255., 128./255.)


#Color maps:
#cmap=plt.cm.gist_stern
#cmap=plt.cm.jet
#cmap=plt.cm.BuPu
#cmap=plt.cm.Spectral
cmap=plt.cm.Set1
#cmap=plt.cm.hsv
#cmap=plt.cm.gist_ncar
#cmap=plt.cm.Accent
#cmap=plt.cm.Dark2
#cmap=plt.cm.PiYG
#cmap=plt.cm.bone
#cmap=plt.cm.RdPu 
#cmap=plt.cm.cool

#Marker codes:
# '+'=>plus sign ; '.'=>dot ; 'o'=>circle ; '*'=>star ; 'p'=>pentagon
# 's'=>square ; 'x'=>x char ; 'D'=>diamond ; 'h'=>hexagon ; '^'=>triangle

#Linesytle codes:
#  '-'=>Solid line ; ':'=>dotted line ; '-.'=>dashed dotted


#//////////////////////////////////////////////////////////////////////////////
#setup & definitions end-------------------------------------------------------
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\



# set up figure and 3D axis for animation
fig = plt.figure(num=1, figsize=(9,9), facecolor=mplot_grey, edgecolor='k')
ax = fig.add_axes([0, 0, 1, 1], projection='3d')
ax.axis('off')
ax.set_axis_bgcolor(mplot_black)

# choose a different color for each trajectory
#colors = plt.cm.jet(np.linspace(0, 1, nTrajectories))
#define color map as variable above
colors = cmap(np.linspace(0, 1, nTrajectories))

# set up lines and points
lines = [l for c in colors for l in ax.plot([], [], [], '-', c=c)]

pts = [pt for c in colors for pt in ax.plot([], [], [], 'o', c=c)]

# prepare the axes limits
ax.set_xlim((-25, 25))
ax.set_ylim((-35, 35))
ax.set_zlim((5, 55))

# set point-of-view: specified by (altitude degrees, azimuth degrees)
ax.view_init(30, 0)

# initializaton function: plot the background of each frame
def init():
    for line, pt in zip(lines, pts):
        line.set_data([], [])
        line.set_3d_properties([])
        
        pt.set_data([], [])
        pt.set_3d_properties([])
    return lines + pts
    
# animation function, this will be called sequentially with the frame number
def animate(i):
    # we'll step two time-steps per frame. This leads to nice results
    i = (2*i)%x_t.shape[1]
    
    for line, pt, xi in zip(lines, pts, x_t):
        x, y, z = xi[:i].T
        line.set_data(x, y)
        line.set_3d_properties(z)
        
        pt.set_data(x[-1:], y[-1:])
        pt.set_3d_properties(z[-1:])
        
    ax.view_init(30, 0.3*i)
    fig.canvas.draw()
    return lines + pts

#anim = animation.FuncAnimation(fig, animate, init_func=init, frames=500, interval=30, blit=True)
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=777, interval=30, blit=True)    
    
# save as .mp4 . This requires ffmpeg or mplayer to be installed
#anim.save('lorenz_attractor.mp4', fps=15, extra_args=['-vcodec', 'libx264'])
anim.save('lorenz_attractor.mp4', fps=20, extra_args=['-vcodec', 'libx264'])
    
plt.show()