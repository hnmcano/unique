from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from windows.form_clients.clientes_ui import Ui_MainWindow
from .AddClientes import AddClientes

def center_window(self):

    screen = QGuiApplication.primaryScreen()
    screen_geometry = screen.availableGeometry()
    window_geometry = self.frameGeometry()

    window_geometry.moveCenter(screen_geometry.center())
    self.move(window_geometry.topLeft())


class Clientes(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        center_window(self)

        self.add_clientes.clicked.connect(self.adicionar_clientes)


    def adicionar_clientes(self):
        self.add_clientes_window = AddClientes(self)
        self.add_clientes_window.show()