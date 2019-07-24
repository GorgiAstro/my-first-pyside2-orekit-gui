from PySide2.QtCore import Qt, QObject, Signal, Slot, Property, QDate, QTime, QDateTime, QUrl

import datetime
import orekit
from orekit.pyhelpers import *
from org.orekit.time import *
from org.orekit.propagation.analytical.tle import *
from org.orekit.attitudes import *
from org.orekit.frames import *
from org.orekit.bodies import *
from org.orekit.utils import *
from org.orekit.models.earth import *
from org.hipparchus.geometry.euclidean.threed import *

class OrbitManager(QObject):
    positionUpdated = Signal()
    propagationFinished = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        # InitVM is required before being able to use Orekit objects
        orekit.initVM()
        setup_orekit_curdir()  # Loads ZIP file containing Orekit data (SPICE kernel, EOP, leap seconds, etc.)

        # Frames
        self._eme2000 = FramesFactory.getEME2000()
        self._itrf = FramesFactory.getITRF(IERSConventions.IERS_2010, True)
        self._wgs84_ellipsoid = ReferenceEllipsoid.getWgs84(self._itrf)
        self._nadir_pointing = NadirPointing(self._eme2000, self._wgs84_ellipsoid)

        # Setup TLE and propagator
        self._tle = TLE('1 25544U 98067A   19205.43407788  .00000753  00000-0  20569-4 0  9999',
                        '2 25544  51.6429 176.4740 0006642 173.2752 328.6116 15.51000066181037')

        self._propagator = SGP4(self._tle,
                                self._nadir_pointing,
                                1000.0)

        self._rx_eme2000 = 0.0
        self._ry_eme2000 = 0.0
        self._rz_eme2000 = 0.0
        self.positionUpdated.emit()

    @Slot()
    def propagateToCurrentTime(self):
        pv_coordinates = self._propagator.getPVCoordinates(datetime_to_absolutedate(datetime.now()),
                                                           self._eme2000)
        pos_eme2000 = pv_coordinates.getPosition()
        self.set_rx_eme2000(1e-3 * pos_eme2000.getX())  # Converting to km
        self.set_ry_eme2000(1e-3 * pos_eme2000.getY())
        self.set_rz_eme2000(1e-3 * pos_eme2000.getZ())
        self.propagationFinished.emit()

    @Property(float, notify=positionUpdated)
    def rx_eme2000(self):
        return self._rx_eme2000

    @rx_eme2000.setter
    def set_rx_eme2000(self, rx_eme2000):
        if rx_eme2000 != self._rx_eme2000:
            self._rx_eme2000 = rx_eme2000
            self.positionUpdated.emit()

    @Property(float, notify=positionUpdated)
    def ry_eme2000(self):
        return self._ry_eme2000

    @ry_eme2000.setter
    def set_ry_eme2000(self, ry_eme2000):
        if ry_eme2000 != self._ry_eme2000:
            self._ry_eme2000 = ry_eme2000
            self.positionUpdated.emit()

    @Property(float, notify=positionUpdated)
    def rz_eme2000(self):
        return self._rz_eme2000

    @rz_eme2000.setter
    def set_rz_eme2000(self, rz_eme2000):
        if rz_eme2000 != self._rz_eme2000:
            self._rz_eme2000 = rz_eme2000
            self.positionUpdated.emit()
