import QtQuick 2.11
import QtQuick.Window 2.2
import QtQuick.Controls 2.4
import QtQuick.Controls.Material 2.4
import QtQuick.Layouts 1.3
import QtQuick.Dialogs 1.3
import LOL.OrbitManager 0.1


Window {
    id: mainWindow
    visible: true

    width: 640
    height: 480
    title: qsTr("My PySide2 GUI")

    /*
     * Instantiates OrbitManager class defined in Python, and connects some of its signals to the GUI
     */
    OrbitManager {
        id: orbitManager
        onPropagationFinished: propNumberTextField.incrementPropNumber()  // Triggered by signal from Python class
    }

    Button {
        id: button
        x: 115
        y: 49
        text: qsTr("Get current ISS position (ECEF)")
        onReleased: orbitManager.propagate(new Date()) // Trigger a slot in the Python class
    }

    TextField {
        id: xPosition
        x: 115
        y: 163
        text: Number(orbitManager.rx_itrf).toFixed(3) // Displays a member variable of the Python class
        horizontalAlignment: Text.AlignHCenter
        readOnly: true
    }

    TextField {
        id: yPosition
        x: 260
        y: 163
        text: Number(orbitManager.ry_itrf).toFixed(3)
        horizontalAlignment: Text.AlignHCenter
        readOnly: true
    }

    TextField {
        id: zPosition
        x: 399
        y: 163
        text: Number(orbitManager.rz_itrf).toFixed(3)
        horizontalAlignment: Text.AlignHCenter
        readOnly: true
    }

    Label {
        id: xLabel
        x: 158
        y: 131
        width: 27
        height: 19
        text: "X"
        horizontalAlignment: Text.AlignHCenter
    }

    Label {
        id: yLabel
        x: 307
        y: 131
        width: 27
        height: 19
        text: "Y"
        horizontalAlignment: Text.AlignHCenter
    }

    Label {
        id: zLabel
        x: 446
        y: 131
        width: 27
        height: 19
        text: "Z"
        horizontalAlignment: Text.AlignHCenter
    }

    TextField {
        id: propNumberTextField
        x: 564
        y: 51
        width: 45
        height: 46
        font.pointSize: 10
        readOnly: true
        property int propNumber;
        text: propNumber
        function incrementPropNumber() {
            propNumber += 1;
        }
    }

    Label {
        id: propNumberLabel
        x: 405
        y: 64
        width: 165
        height: 19
        text: qsTr("Number of propagations:")
        font.pointSize: 10
    }

}
