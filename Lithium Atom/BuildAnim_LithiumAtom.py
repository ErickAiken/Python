#Lithium Atom - Animation
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
#import matplotlib
#matplotlib.use("agg")

#Update Lines
def UpdateLines(n, datalines, lines):
    for line, data in zip(lines, datalines):
        line.set_data(data[0:2, 0:n])
        line.set_3d_properties(data[2, 0:n])
    return lines

#Build 3d Animation    
def Animation3D(position):
    #Attaching 3d axis to figure
    fig = plt.figure()
    ax = p3.Axes3D(fig)
    time = position.shape[1]
    data = []
    data.append(position)
    
    #Trajectories of the N particles 3d lines
    lines = [ax.plot(dat[0, 0:1], dat[1, 0:1], dat[2, 0:1], 'o')[0] for dat in data]
    
    #Setting the axes properties
    ax.set_xlim3d([-10.0, 10.0])
    ax.set_xlabel('X')
    ax.set_ylim3d([-10.0, 10.0])
    ax.set_ylabel('Y')
    ax.set_zlim3d([-10.0, 10.0])
    ax.set_zlabel('Z')
    ax.set_title('Electron in Motion')
    
    #Creating the Animation Object
    line_ani = animation.FuncAnimation(fig, UpdateLines, time, fargs=(data, lines), interval=50, blit=True)
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
    line_ani.save('ElectronLithiumAtom.mp4', writer=writer)
    plt.show()
    print("Done")
