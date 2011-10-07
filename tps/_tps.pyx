# Copyright (c) 2011, Omniscale GmbH & Co. KG
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

cdef extern from "thinplatespline.h":
    cdef cppclass VizGeorefSpline2D:
        VizGeorefSpline2D(int)
        int get_nof_points()
        void add_point(double, double, double *)
        void get_point(double, double, double *)
        int solve()


class TPSError(Exception):
    pass

cdef class TPS:
    """
    Thin Plate Spline computation class.
    
    >>> t = TPS()
    >>> t.add(0, 0, 50, 50)
    >>> t.add(10, 10, 100, 100)
    >>> t.transform(4, 5)
    (72.5, 72.5)
    >>> t.add(0, 10, 70, 100)
    >>> t.transform(4, 5)
    (72.0, 75.0)
    """
    cdef VizGeorefSpline2D *_sp
    cdef bint _solved
    def __cinit__(self, points=None):
        self._sp = new VizGeorefSpline2D(2)
        self._solved
        if points:
            for p in points:
                self.add(*p)
        
    def add(self, double src_x, double src_y, double dst_x, double dst_y):
        """
        Add a control point for the TPS.
        
        :param src_x: x value of the source point
        :param src_y: y value of the source point
        :param dst_x: x value of the destination point
        :param dst_y: y value of the destination point
        """
        cdef double dst[2]
        dst[0] = dst_x
        dst[1] = dst_y
        self._sp.add_point(src_x, src_y, dst)
        self._solved = False
    
    def solve(self):
        """
        Calculate TPS. Raises TPSError if TPS could not be solved.
        """
        result = self._sp.solve()
        if not result:
            raise TPSError('could not solve thin plate spline')
        self._solved = True
    
    def transform(self, double src_x, double src_y):
        """
        Transform from source point to destination.
        
        :param src_x: x value of the source point
        :param src_y: y value of the source point
        :returns: x and y values of the transformed point
        """
        if not self._solved:
            self.solve()
        cdef double dst[2]
        self._sp.get_point(src_x, src_y, dst)
        return dst[0], dst[1]

def from_control_points(points, backwards=False):
    t = TPS()
    for p in points:
        if backwards:
            t.add(p[2], p[3], p[0], p[1])
        else:
            t.add(*p)
    
    return t