import matplotlib.pyplot as plt   
import numpy as np


class Coordinate:
  def __init__(self, x: str or float, y: str or float, anomaly: bool = False):
    self.x = float(x)
    self.y = float(y)
    self.anomaly = False if anomaly is None else anomaly

  def __str__(self):
    return str((self.x,self.y))



class Line:
  def __init__(self, list_of_coords: list):
    self.x_points = []
    self.y_points = []
    self.invalid_x_points=[]
    self.invalid_y_points = []
    for coord in list_of_coords:
      if coord.anomaly == False:
        self.x_points.append(coord.x)
        self.y_points.append(coord.y)
      else:
        self.invalid_x_points.append(coord.x)
        self.invalid_y_points.append(coord.y)


    
  def plot(self):
    try:
      p= np.polyfit(self.x_points, self.y_points, 1)
    except TypeError:
      raise IndexError("number of points must be more than 1")
    
    f = np.polyval(p,self.x_points); 
    plt.plot(self.x_points,f,'-') 
    plt.plot(self.x_points+self.invalid_x_points,self.y_points+self.invalid_y_points,'o')
    plt.show()





#plots coordinates in a txt file
def plot_file(path: str, anomaly_check):
  if not callable(anomaly_check):
    raise TypeError("anomaly_check must be a function that has arguments: (x,y) which returns True if the point is an anomaly. ")
  with open(path,"r") as f:
    
    points = []
    file =f.readlines()
    line = 0
    for coord in file:
      line+=1
      coord.replace('\n','')
      try:
        x,y = coord.split(",")
        
      except ValueError:
        raise ValueError(f"expected 2 strings separated with ',', got '{coord}' in line: {line}")
      try:
        coord = Coordinate(x,y, anomaly_check(float(x),float(y)))
      except ValueError:
        raise TypeError(f"expected strings to be able to be converted to float, got {x,y} in line: {line}")
      
      points.append(coord)
    f.close()
    line = Line(points)
    line.plot()

#uses a list of tuples as coordinates
def plot_raw(coords:list, anomaly_check):
  points = []
  if not callable(anomaly_check):
    raise TypeError("anomaly_check must be a function that has arguments: (x,y) which returns True if the point is an anomaly. ")
  for coord in coords:
    if not isinstance(coord, tuple):
      raise TypeError("all coodinates in provided list must be tuple")
    if len(coord) !=2:
      raise IndexError("all coordinates must only have length of 2 in form (x,y)")
    x,y = coord
    print(coord)
    coord = Coordinate(x,y, anomaly_check(int(x),int(y)))
    points.append(coord)
  line = Line(points)
  line.plot()






