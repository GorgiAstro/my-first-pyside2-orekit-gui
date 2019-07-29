import sys
import os

from PySide2.QtWidgets import QApplication
from PySide2.QtQml import qmlRegisterType, QQmlApplicationEngine
from PySide2.QtGui import QIcon

from orbitmanager import OrbitManager

if __name__ == "__main__":
    """
    Main python file
    Register the Python class OrbitManager to the QML system.
    Then load the QML application engine and fire up the GUI
    """

    sys_argv = sys.argv
    sys_argv += ['--style', 'material']
    # Create QApplication
    app = QApplication(sys_argv)
    app.setWindowIcon(QIcon('logo.png'))

    # Register Python classes in QML
    qmlRegisterType(OrbitManager, 'LOL.OrbitManager', 0, 1, 'OrbitManager')

    # Start QML engine
    engine = QQmlApplicationEngine()
    engine.load('main.qml')

    win = engine.rootObjects()[0]
    win.show()
    sys.exit(app.exec_())
