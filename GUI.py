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

class App(QtWidgets.QMainWindow):
    """"The App class inherits from the QMainWindow. It acts as a container for the MainWindow class
        (QWidget) while also setting the window title and creating the statusbar."""

    def __init__(self):
        super().__init__()

        # Setting the window title and assigning the MainWindow class as the central widget.
        self.setWindowTitle("Quanta")
        self.setWindowIcon(QtGui.QIcon("Icon.png"))
        self.MainWindow = MainWindow(self)
        self.setCentralWidget(self.MainWindow)

        # Creating the Statusbar.
        StatusBar = self.statusBar()
        StatusBar.showMessage('Ready')

        # Creating the toolbar.
        self.Toolbar = self.addToolBar("Toolbar")
        self.Toolbar.setMovable(False)

        # Creating the progressbar.
        self.ProgressBar = QtWidgets.QProgressBar(self)

        # Adding widgets and buttons(actions) to the toolbar.
        self.Toolbar.addWidget(self.ProgressBar)

        # Displaying the Graphical User Interface.
        self.show()

class MainWindow(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Creating instances of the tabs within the MainWindow class.
        Tabs = QtWidgets.QTabWidget()
        self.ViewTab = ViewTab()
        self.ConsoleTab = ConsoleTab()
        self.ParametersTab = ParametersTab()

        # Creating the QTabWidget and adding the instances of the tabs to it.
        Tabs = QtWidgets.QTabWidget()
        Tabs.addTab(self.ViewTab, "View")
        Tabs.addTab(self.ConsoleTab, "Console")
        Tabs.addTab(self.ParametersTab, "Parameters")

        # Creating the layout for the MainWindow class.
        Layout = QtWidgets.QVBoxLayout()
        self.setLayout(Layout)

        # Adding all widgets to the MainWindow class through the layout scheme.
        Layout.addWidget(Tabs)

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

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    GUI = App()
    app.exec_()


