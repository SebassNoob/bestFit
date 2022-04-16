================
bestFit
================

About
=====
bestFit is a module that uses matplotlib and numpy to plot the best fit line of a given set of coordinates.

github page: https://github.com/SebassNoob/bestFit

Quickstart
==========
This is how to plot a basic graph based on a list of coordinates.

1. Create a file named ``index.py`` in root
2. To import the module, use ``import bestFit.main as bf`` (or any similar shorthand)
3. Define a list of coordinates, for example: ``my_coords = [(0,0),(1,3),(2,3),(4,7),(8,0),(-1,0.33)]`` 
4. Plot the graph like this:

.. code-block:: python

  import bestFit.main as bf
	
  my_coords = [(0,0),(1,3),(2,3),(4,7),( 8,0),(-1,0.33)]
  
	def check_for_anomaly(x,y):
	#checks for anomalies in points, eg: if the x coordinate of a given point is >1000, return True else return False (or None)
	if x>1000:
		return True
  	return None
  line = bf.create_line_from_raw(line_name="mygraph",linestyle="g-",pointstyle="go"coords = my_coords, n_power =1 , anomaly_check = check_for_anomaly)
  line.plot()
  show_graph()
  
5. Then, run in console: ``python3 index.py``
6. A line with name ``mygraph`` a green solid plotted line, and points on that line displayed as green circles, sould be shown. 


Classes
=========

``class Coordinate(x: str or float, y: str or float, anomaly: bool = False)``
=============

The basic coordinate: contains a x and y variable, as well as if the coordinate is an anomaly. 

Anomaly values are ignored when plotting a best fit line.

Attributes:
-------

``x`` (float)

A x coordinate.

``y`` (float)

A y coordinate.

``anomaly`` (bool, optional)

Defaults to False. If True, point is considered an anomaly and will not be taken into consideration when plotting.

Methods:
-------
``__str__``

returns (x,y)



``class Line(list_of_coords: list, n_power: int)``
========

A Line object. ``list_of_coords`` is a list containing Coordinate objects.

``n_power`` refers to the polynomial power when finding the best fit line. For example, when ``n_power = 1``, Line is linear in the form y = mx + c, but when ``n_power = 2``, Line is a curve in the form y=ax^2 + bx + c.

Attributes:
----------

``name`` (str)

The name of the line used and displayed in the legend.
This defaults to a string of ``numpy.ndarray`` with the coefficients of the line.

``linestyle`` (str) and ``pointstyle``

The style of the best fit line and the points plotted. Defaults to "-" and "o" respectively.
Available types:

#show img here

eg:

:: 

  "b-" => a blue solid line
  "w-." => a white dash-dot line
  "ro" => red circle markers
  "kx" => black x markers
  

``x_points`` (list)

A list of x points provided

``y_points`` (list)

A list of y points provided

``invalid_x_points`` (list)

A list of x points that are considered "anomalies". See Coordinate class.

``invalid_y_points`` (list)

A list of y points that are considered "anomalies". See Coordinate class.

``polynomial_coefficients`` (numpy.ndarray)

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
--------
``calculate()``

Based on given valid points, this will find the coefficients of the polynomial of the best fit line, then calculate ``solved_x`` and ``solved_y``, then sort.

returns None

``smoothen_line(accuracy: int= None)``

Smooths a line. Useful when ``n_power > 1``

returns (self.solved_x, self.solved_y)

``plot()``

Plots the line, but does not show it.

returns None

``add_point(coord: Coordinate)``

Adds a point to the Line object. Parameter passed must be a Coordinate object. eg. ``line.add_point(Coordinate(1,2))``

returns None

``remove_point(coord: Coordinate)``

Removes a point from the Line object. Parameter passed must be a Coordinate object. eg. ``line.remove_point(Coordinate(6,9))``

returns None

Functions
===========

``create_line_from_file(*,line_name:str =None,linestyle = None,pointstyle=None, path: str, n_power: int=1, anomaly_check=None)``
=============
Creates a line from a .txt (only) file.
An example of a txt file:

::

  1,2
  3,4
  5,6
  -1.2,4
  0,0

line_name (str, optional): the name of the line to be shown on the legend. Defaults to the coefficients of the polynomial of the line.

linestyle (str): The style of the line. See the Line.linestyle attribute for list of accepted styles.

pointstyle (str): The style of the points. See the Line.pointstyle attribute for list of accepted styles.

path (str): the path to your file

n_power (int, optional): the n_power of your line (See Line object)

anomaly_check (function, optional): a function of parameters (x,y). Checks if a point specified is invalid and returns True if so.

eg.

.. code-block:: python

  def check(x,y):
    if y>0:
      return True
    return False

Returns a ``Line()`` object.


``create_line_from_raw(*,line_name:str =None,linestyle = None, pointstyle = None,coords:list, n_power: int=1, anomaly_check=None)`` 
===================
Creates a line from a list of tuples containing x,y points.

coords (list): list of coords

eg. ``hi = [(0,0),(1,1),(2,3)]``

line_name (str, optional): the name of the line to be shown on the legend. Defaults to the coefficients of the polynomial of the line.

linestyle (str): The style of the line. See the Line.linestyle attribute for list of accepted styles.

pointstyle (str): The style of the points. See the Line.pointstyle attribute for list of accepted styles.

n_power (int, optional): the n_power of your line (See Line object)

anomaly_check (function, optional): a function of parameters (x,y). Checks if a point specified is invalid and returns True if so.

eg.

.. code-block:: python

  def check(x,y):
    if y>0:
      return True
    return False


Returns a ``Line()`` object.

The end:)
