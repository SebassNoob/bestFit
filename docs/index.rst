================
bestFit
================

About
=====
bestFit is a module that uses matplotlib and numpy to plot the best fit line of a given set of coordinates.

Quickstart
==========
This is how to plot a basic graph based on a list of coordinates.

1. Create a file named ``index.py``
2. To import the module, use ``import bestFit.main as bf`` (or any similar shorthand)
3. Define a list of coordinates, for example: ``my_coords = [(0,0),(1,3),(2,3),(4,7),(8,0),(-1,0.33)]`` 
4. Plot the graph like this:

.. code-block:: python3
import bestFit.main as bf
my_coords = [(0,0),(1,3),(2,3),(4,7),(8,0),(-1,0.33)]
def check_for_anomaly(x,y):
  return None
line = bf.create_line_from_raw(coords = my_coords, n_power =1 , anomaly_check = check_for_anomaly)
line.plot()::



Documentation
=============


CLASSES
--------

``class Coordinate(x: str or float, y: str or float, anomaly: bool = False)``


The basic coordinate: contains a x and y variable, as well as if the coordinate is an anomaly. 

Anomaly values are ignored when plotting a best fit line.

Attributes:

``x`` (float)

A x coordinate.

``y`` (float)

A y coordinate.

``anomaly`` (bool)

Defaults to False. If True, point is considered an anomaly and will not be taken into consideration when plotting.

Methods:

``__str__``

returns (x,y)



``class Line(list_of_coords: list, n_power: int)``


A Line object. ``list_of_coords`` is a list containing Coordinate objects.

``n_power`` refers to the polynomial power when finding the best fit line. For example, when ``n_power = 1``, Line is linear in the form y = mx + c, but when ``n_power = 2``, Line is a curve in the form y=ax^2 + bx + c.

Attributes:

``x_points`` (list)

A list of x points provided

``y_points`` (list)

A list of y points provided

``invalid_x_points`` (list)

A list of x points that are considered "anomalies". See Coordinate class.

``invalid_y_points`` (list)

A list of y points that are considered "anomalies". See Coordinate class.

``polynomial_coefficients`` (list-like)

The coefficients to the solved line equation. eg. [1.0 2.0 3.0] is x^2 + 2x + 3

``solved_y`` (list)

Defaults to y_points. If smoothen_graph is called (See smoothe_graph class function), this will contain more values for y solved with polynomial_coefficients.

``solved_x`` (list)

Defaults to x_points. If smoothen_graph is called (See smoothe_graph class function), this will contain more values for x solved with polynomial_coefficients.

``self.smoothness`` (int)

The "smoothness" of the graph. A greater value means more smooth.

``n`` (int)

The power of n used for calculation.


Methods:

``smoothen_graph(accuracy: int= None)``

Smooths a graph. Useful when ``n_power > 1``

returns (self.solved_x, self.solved_y)

``plot()``

Plots the graph.

returns None

``add_point(coord: Coordinate)``

Adds a point to the Line object. Parameter passed must be a Coordinate object. eg. ``line.add_point(Coordinate(1,2))``

returns None

``remove_point(coord: Coordinate)``

Removes a point from the Line object. Parameter passed must be a Coordinate object. eg. ``line.remove_point(Coordinate(6,9))``

returns None

FUNCTIONS
---------

``create_line_from_file(*,path: str, n_power: int=1, anomaly_check)``

Creates a line from a .txt (only) file.
An example of a txt file:

___BEGIN TXT FILE___

1,2

3,4

5,6

-1.2,4

0,0

___END TXT FILE___

path: the path to your file

n_power: the n_power of your line (See Line object)

anomaly_check: a function of parameters (x,y). Checks if a point specified is invalid and returns True if so.

eg.

.. code-block:: python3
def check(x,y):
  if y>0:
    return True
  return False::

``create_line_from_raw(*,coords:list, n_power: int, anomaly_check)``

Creates a line from a list of tuples containing x,y points.

coords: list of coords

eg. ``hi = [(0,0),(1,1),(2,3)]``

n_power: the n_power of your line (See Line object)

anomaly_check: a function of parameters (x,y). Checks if a point specified is invalid and returns True if so.

eg.

.. code-block:: python3
def check(x,y):
  if y>0:
    return True
  return False::


The end:)