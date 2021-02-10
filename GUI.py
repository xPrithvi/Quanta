# Importing modules from the Python Standard Library.
import sys
import math

# Importing third-party modules.
import numpy as np

# Importing Matplot's Python Library.
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

# Importing PyQt5.
from PyQt5 import QtCore, QtWidgets, QtGui

class MainWindow(QtWidgets.QMainWindow):
    """"The MainWindow class inherits from the QMainWindow. It acts as a container for the MainWindow class
        (QWidget) while also setting the window title and creating the statusbar."""

    def __init__(self):
        super().__init__()

        # Setting the window title, icon, and assigning the MainWindow class as the central widget.
        self.setWindowTitle("Quanta")
        self.setWindowIcon(QtGui.QIcon("Icon.png"))

        # Creating instances of the tabs within the QMainWindow class.
        self.ViewTab = ViewTab()
        self.ConsoleTab = ConsoleTab()
        self.ParametersTab = ParametersTab()

        # Creating the QTabWidget and adding the instances of the tabs to it.
        Tabs = QtWidgets.QTabWidget()
        Tabs.addTab(self.ViewTab, "View")
        Tabs.addTab(self.ConsoleTab, "Console")
        Tabs.addTab(self.ParametersTab, "Parameters")
        self.setCentralWidget(Tabs)

        # Creating the Statusbar.
        StatusBar = self.statusBar()
        StatusBar.showMessage('Ready')

        # Creating the toolbar.
        self.Toolbar = self.addToolBar("Toolbar")
        self.Toolbar.setMovable(False)

        # Creating the progressbar.
        self.ProgressBar = QtWidgets.QProgressBar(self)

        # Creating buttons.
        self.UpdateView = QtWidgets.QAction("Update View", self)

        # Adding widgets and buttons(actions) to the toolbar.
        self.Toolbar.addAction(self.UpdateView)
        self.Toolbar.addWidget(self.ProgressBar)

        # Buttons are connected to their respective handlers.
        self.UpdateView.triggered.connect(MainWindow.UpdateView_handler)

        # Displaying the Graphical User Interface.
        self.show()

    def UpdateView_handler():

        # Console output.
        print("Event: UpdateView_handler")

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        figure = Figure(figsize=(width, height), dpi=dpi)
        self.axes = figure.gca(projection='3d')
        super(MplCanvas, self).__init__(figure)

class ViewTab(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.length_x = 1
        self.length_y = 1
        self.quantum_number_x = 3
        self.quantum_number_y = 2

        """Generating x-coordinates."""
        x = np.linspace(0, self.length_x, 100)

        """Generating y-coordinates."""
        y = np.linspace(0, self.length_y, 100)

        """Generating all possible xy-coordinates."""
        X,Y = np.meshgrid(x,y)

        """Generating z-coordinates from xy-coordinates."""
        Z = np.sqrt((2)/(self.length_x*self.length_y))*np.sin((math.pi*self.quantum_number_x*X)/(self.length_x))*np.sin((math.pi*self.quantum_number_y*Y)/(self.length_y))

        plt = MplCanvas(self, width=5, height=4, dpi=100)
        contour = plt.axes.plot_surface(X,Y,Z,cmap='hot')
        plt.figure.colorbar(contour, shrink = 1)
        plt.axes.view_init(elev = 20, azim = -135)
        plt.axes.set_xlabel(r'$x$')
        plt.axes.set_ylabel(r'$y$')
        plt.axes.set_zlabel(r'$\psi(x, y)$')
        Layout = QtWidgets.QVBoxLayout()
        Layout.addWidget(plt)
        self.setLayout(Layout)

class ConsoleTab(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        # Creating the Console(QTextBrowser class) within the ConsoleTab(QTabWidget class).
        self.Textbox = QtWidgets.QTextBrowser(self)
        self.Textbox.setReadOnly(True)
        self.Textbox.setOpenExternalLinks(True)

        # Adding the Console(QTextBrowser class) to the layout ConsoleTab(QTabWidget class)..
        Layout = QtWidgets.QVBoxLayout()
        Layout.addWidget(self.Textbox)
        self.setLayout(Layout)

        # Printing starting text.
        self.Textbox.insertPlainText("===========================")
        self.Textbox.insertPlainText("\n")
        self.Textbox.insertHtml("<b> Quanta Version: 0.0.1 </b>")
        self.Textbox.insertPlainText("\n")
        self.Textbox.insertHtml("<b> Created by Prithvi R. </b>")
        self.Textbox.insertPlainText("\n")
        self.Textbox.insertPlainText("======================")

class ParametersTab(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        GridLayout = QtWidgets.QGridLayout()
        self.setLayout(GridLayout)

        Group = QtWidgets.QGroupBox("Quantum System")
        self.QuantumSystem = QtWidgets.QComboBox(self)
        self.QuantumSystem.resize(200, 25)
        self.QuantumSystem.addItem("Particle in a Box (2D)")
        GridLayout.addWidget(Group)

        self.QuantumFunction = QtWidgets.QComboBox(self)
        self.QuantumFunction.resize(200, 25)
        self.QuantumFunction.addItem("Wavefunction")
        self.QuantumFunction.addItem("Probability Density Function")

        GridLayout.addWidget(Group)
        GroupLayout = QtWidgets.QVBoxLayout()
        GroupLayout.addWidget(self.QuantumSystem)
        GroupLayout.addWidget(self.QuantumFunction)
        Group.setLayout(GroupLayout)

if __name__ == "__main__":
    application = QtWidgets.QApplication(sys.argv)
    GUI = MainWindow()
    application.exec_()
