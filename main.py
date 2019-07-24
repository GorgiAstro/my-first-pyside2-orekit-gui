import sys
import os

from PySide2.QtWidgets import QApplication
from PySide2.QtQml import qmlRegisterType, QQmlApplicationEngine
from PySide2.QtGui import QIcon

from orbitmanager import OrbitManager

if __name__ == "__main__":
    """
    Main python file
    It registers the Python class OrbitManager to the QML system.
    Then it loads the QML application engine and fires up the GUI
    """

    current_path = os.path.abspath(os.path.dirname(__file__))
    qml_file = os.path.join('main.qml')

    sys_argv = sys.argv
    sys_argv += ['--style', 'material']
    app = QApplication(sys_argv)
    app.setWindowIcon(QIcon('logo.png'))

    # Register Python classes in QML
    qmlRegisterType(OrbitManager, 'LOL.OrbitManager', 0, 1, 'OrbitManager')

    engine = QQmlApplicationEngine()
    engine.load(qml_file)

    win = engine.rootObjects()[0]
    win.show()
    sys.exit(app.exec_())