from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import style
import math

class ParticleInABox():

    class OneDimensional():

        def __init__(self, length_x, quantum_number):

            self.length_x = length_x
            self.quantum_number = quantum_number

        def wavefunction(self):

            x = []
            for i in range((self.length_x)*100):
                u = i/100
                x.append(u)
        
            y = []

            for i in x:
                output = math.sqrt((2)/(self.length_x))*math.sin((math.pi*self.quantum_number*i)/(self.length_x))
                y.append(output)

            plt.plot(x, y)
            plt.show()

        def PDF(self):

            x = []
            for i in range((self.length_x)*100):
                u = i/100
                print(u)
                x.append(u)

            y = []

            for i in x:
                output = (2/self.length_x)*pow(math.sin((math.pi*self.quantum_number*i)/(self.length_x)), 2)
                y.append(output)

            plt.plot(x, y)
            plt.xlabel('\\alpha')
            plt.ylabel('\\beta')
            plt.show()

    class TwoDimensional():

        def __init__(self, length_x, length_y, quantum_number):

            self.length_x = length_x
            self.length_y = length_y
            self.quantum_number = quantum_number

        def wavefunction(self):

            """Generating x-coordinates."""
            x = []
            for i in range((self.length_x)*100):
                u = i/100
                x.append(u)

            """Generating y-coordinates."""
            y = []
            for i in range((self.length_y)*100):
                u = i/100
                y.append(u)

            """Generating all possible xy-coordinates."""
            surface_coordinates = []
            for i in x:
                for j in y:
                    coordinate = []
                    coordinate.append(i)
                    coordinate.append(j)
                    surface_coordinates.append(coordinate)

            """Generating z-coordinates from xy-coordinates."""
            for coordinate in surface_coordinates:
                output = math.sqrt((2)/(self.length_x*self.length_y))*math.sin((math.pi*self.quantum_number*coordinate[0])/(self.length_x))*math.sin((math.pi*self.quantum_number*coordinate[1])/(self.length_y))
                coordinate.append(output)

            """Formatting xyz-coordinates."""
            x_plot = []
            y_plot = []
            z_plot = []
            for coordinate in surface_coordinates:
                x_plot.append(coordinate[0])
                y_plot.append(coordinate[1])
                z_plot.append(coordinate[2])

            """Generating plot."""
            fig = plt.figure()
            ax1 = fig.add_subplot(111, projection='3d')
            ax1.plot(x_plot, y_plot, z_plot)
            ax1.set_xlabel('x axis')
            ax1.set_ylabel('y axis')
            ax1.set_zlabel('z axis')
            plt.show()

        def PDF(self):

            """Generating x-coordinates."""
            x = []
            for i in range((self.length_x)*100):
                u = i/100
                x.append(u)

            """Generating y-coordinates."""
            y = []
            for i in range((self.length_y)*100):
                u = i/100
                y.append(u)

            """Generating all possible xy-coordinates."""
            surface_coordinates = []
            for i in x:
                for j in y:
                    coordinate = []
                    coordinate.append(i)
                    coordinate.append(j)
                    surface_coordinates.append(coordinate)

            """Generating z-coordinates from xy-coordinates."""
            for coordinate in surface_coordinates:
                output = (2/self.length_x*self.length_y)*pow(math.sin((math.pi*self.quantum_number*coordinate[0])/(self.length_x))*math.sin((math.pi*self.quantum_number*coordinate[1])/(self.length_y)),2)
                coordinate.append(output)

            """Formatting xyz-coordinates."""
            x_plot = []
            y_plot = []
            z_plot = []
            for coordinate in surface_coordinates:
                x_plot.append(coordinate[0])
                y_plot.append(coordinate[1])
                z_plot.append(coordinate[2])

            """Generating plot."""
            fig = plt.figure()
            ax1 = fig.add_subplot(111, projection='3d')
            ax1.plot(x_plot, y_plot, z_plot)
            ax1.set_xlabel('x axis')
            ax1.set_ylabel('y axis')
            ax1.set_zlabel('z axis')
            plt.show()

    class ThreeDimensional():

        def __init__(self, length_x, length_y, length_z, quantum_number, scatter_density):

            self.length_x = length_x
            self.length_y = length_y
            self.length_z = length_z
            self.quantum_number = quantum_number
            self.scatter_density = scatter_density

        def wavefunction(self):

            """Generating x-coordinates."""
            x = []
            for i in range((self.length_x)*self.scatter_density):
                u = i/self.scatter_density
                x.append(u)

            """Generating y-coordinates."""
            y = []
            for i in range((self.length_y)*self.scatter_density):
                u = i/self.scatter_density
                y.append(u)

            """Generating z-coordinates."""
            z = []
            for i in range((self.length_z)*self.scatter_density):
                u = i/self.scatter_density
                z.append(u)

            """Generating all possible xyz-coordinates."""
            space_coordinates = []
            counter = 0
            for i in x:
                for j in y:
                    for k in z:
                        coordinate = []
                        coordinate.append(i)
                        coordinate.append(j)
                        coordinate.append(k)
                        space_coordinates.append(coordinate)
                        counter = counter + 1

            """Generating colour-coordinates from xyz-coordinates."""
            for coordinate in space_coordinates:
                output = math.sqrt((2)/(self.length_x*self.length_y*self.length_z))*math.sin((math.pi*self.quantum_number*coordinate[0])/(self.length_x))*math.sin((math.pi*self.quantum_number*coordinate[1])/(self.length_y))*math.sin((math.pi*self.quantum_number*coordinate[2])/(self.length_z))
                coordinate.append(output)

            """Formatting colour-xyz-coordinates."""
            x_plot = []
            y_plot = []
            z_plot = []
            colour_plot = []
            for coordinate in space_coordinates:
                x_plot.append(coordinate[0])
                y_plot.append(coordinate[1])
                z_plot.append(coordinate[2])
                colour_plot.append(coordinate[3])

            """Generating plot"""
            fig = plt.figure()
            ax1 = fig.add_subplot(111, projection='3d')
            img = ax1.scatter(x_plot, y_plot, z_plot, c=colour_plot, cmap=plt.get_cmap('jet'))
            fig.colorbar(img)
            ax1.set_xlabel('x axis')
            ax1.set_ylabel('y axis')
            ax1.set_zlabel('z axis')
            plt.show()

        def PDF(self):

            """Generating x-coordinates."""
            x = []
            for i in range((self.length_x)*self.scatter_density):
                u = i/self.scatter_density
                x.append(u)

            """Generating y-coordinates."""
            y = []
            for i in range((self.length_y)*self.scatter_density):
                u = i/self.scatter_density
                y.append(u)

            """Generating z-coordinates."""
            z = []
            for i in range((self.length_z)*self.scatter_density):
                u = i/self.scatter_density
                z.append(u)

            """Generating all possible xyz-coordinates."""
            space_coordinates = []
            counter = 0
            for i in x:
                for j in y:
                    for k in z:
                        coordinate = []
                        coordinate.append(i)
                        coordinate.append(j)
                        coordinate.append(k)
                        space_coordinates.append(coordinate)
                        counter = counter + 1

            """Generating colour-coordinates from xyz-coordinates."""
            for coordinate in space_coordinates:
                output = (2/(self.length_x*self.length_y*self.length_z))*pow(math.sin((math.pi*self.quantum_number*coordinate[0])/(self.length_x))*math.sin((math.pi*self.quantum_number*coordinate[1])/(self.length_y))*math.sin((math.pi*self.quantum_number*coordinate[2])/(self.length_z)),2)
                coordinate.append(output)

            """Formatting colour-xyz-coordinates."""
            x_plot = []
            y_plot = []
            z_plot = []
            colour_plot = []
            for coordinate in space_coordinates:
                x_plot.append(coordinate[0])
                y_plot.append(coordinate[1])
                z_plot.append(coordinate[2])
                colour_plot.append(coordinate[3])

            """Generating plot"""
            fig = plt.figure()
            ax1 = fig.add_subplot(111, projection='3d')
            img = ax1.scatter(x_plot, y_plot, z_plot, c=colour_plot, cmap=plt.get_cmap('jet'))
            fig.colorbar(img)
            ax1.set_xlabel(r'$L_x$')
            ax1.set_ylabel(r'$L_y$')
            ax1.set_zlabel(r'$L_z$')
            plt.show()

ParticleInABox().ThreeDimensional(length_x = 1, length_y = 1, length_z = 1, quantum_number = 1, scatter_density = 13).PDF()
