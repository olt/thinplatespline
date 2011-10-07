TPS
===

Python library to create Thin-Plate-Splines from control points.

It uses code from the GDAL Warp API, but there is no dependency to GDAL.

::

  from tps import from_control_points

  >>> t = from_control_points([
  ...   (0, 0, 50, 50),
  ...   (10, 10, 100, 100),
  ...   (0, 10, 70, 100)])
  >>> t.transform(4, 5)
  (72.0, 75.0)