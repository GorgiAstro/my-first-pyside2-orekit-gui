# Description

This provides an example of a basic GUI in Python based on PySide2 (Qt for Python) and relying on QML & Qt Quick Controls 2 widgets.
This GUI uses Orekit to compute the current position of the ISS.

# Installation

## Prerequisites
* Anaconda or Miniconda

## Install conda environment

Install the conda environment. For this, you can either import the environment.yml file into Anaconda Navigator, or use the command line
`conda env create -f environment.yml`

# Enter conda environment
source activate mycondaenv

# Run GUI
`python main.py`

# Workflow in the Python code
Open the folder in PyCharm for instance. 

Make sure to setup the proper project interpreter from the conda environment. You can then run and debug your Python code as a normal Python project (but not the QML code).

# Workflow in the QML code
Open `qml-project.qmlproject` in QtCreator. The GUI is defined in the `main.qml` file.

However, I could not manage to make the QML interpreter in QtCreator recognize the Python classes. Therefore to be able to use the "Design Mode" without having errors, one must comment out the import statements for the Python classes, e.g. `// import LOL.OrbitManager 0.1`.

It is also not possible to execute the Python project from QtCreator (or at least, not that I know of).