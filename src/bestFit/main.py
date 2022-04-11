import matplotlib.pyplot as plt   
import numpy as np
import math
import statistics

class Coordinate:
  def __init__(self, x: str or float, y: str or float, anomaly: bool = False):
    self.x = float(x)
    self.y = float(y)
    self.anomaly = False if anomaly is None else anomaly

  def __str__(self):
    return str((self.x,self.y))


#a set of coordinates
class Line:
  def __init__(self, list_of_coords: list, n_power: int):
    self.x_points = []
    self.y_points = []
    self.invalid_x_points=[]
    self.invalid_y_points = []
    self.polynomial_coefficients = self.solved_y=self.solved_x =self.smoothness= None
    self.n = n_power
    for coord in list_of_coords:
      if coord.anomaly == False:
        self.x_points.append(coord.x)
        self.y_points.append(coord.y)
      else:
        self.invalid_x_points.append(coord.x)
        self.invalid_y_points.append(coord.y)

    
    try:
      #array? of a,b,c... in ax^n + bx^n-1 + cx^n-2... 
      self.polynomial_coefficients = np.polyfit(self.x_points, self.y_points, self.n)


    except TypeError:
      raise IndexError("number of points must be >= 1")
    #default value of solved x and y
    self.solved_y = np.polyval(self.polynomial_coefficients,self.x_points)
    self.solved_x = self.x_points


  

  def smoothen_graph(self, accuracy: int= None):
    if accuracy ==None:
      return
    # defines maximum x point and minimum x point
    range_max, range_min = (sorted(self.x_points)[len(self.x_points)-1],sorted(self.x_points)[0])
    #finds avg interval betweeen points so i that accuracy is relative to interval
    average_dist=[]
    for i in range(len(self.x_points)):
      
      try:
        
        average_dist.append(self.x_points[i+1] - self.x_points[i])
      except IndexError:
        break


    mean = abs(statistics.mean(average_dist))
    new_points = []
    
    while range_min <= range_max:
      
      range_min+= mean/accuracy
      new_points.append(range_min)




    
    #solves for y given eqn and x
    self.smoothness = accuracy
    self.solved_x = new_points
    self.solved_y = np.polyval(self.polynomial_coefficients,new_points)

    return (self.solved_x, self.solved_y)

  #actually plots a line 
  def plot(self):
    
    plt.plot(self.solved_x,self.solved_y,'-') 

    plt.plot(self.x_points+self.invalid_x_points,self.y_points+self.invalid_y_points,'o')
    plt.show()

    return 


  
    
  def add_point(self,coord: Coordinate):
    if coord.anomaly == False:
      self.x_points.append(coord.x)
      self.y_points.append(coord.y)
    else:
      self.invalid_x_points.append(coord.x)
      self.invalid_y_points.append(coord.y)

    return




    
  def remove_point(self, coord: Coordinate):
    x_points = sorted(self.x_points)
    y_points = sorted(self.y_points)

    #in case of repeat points, a linear search is better
    #however start from the back if value of midpoint is smaller than value to remove
    #time = O(n/2)
    
    def linear_search(coord):
      midpoint_value_x = x_points[math.floor(len(x_points)/2)]
      if coord.x < midpoint_value_x:
        for i in range(len(x_points)):
          if x_points[i] == coord.x and y_points[i] == coord.y:
            return (x_points[i],y_points[i])
            #returns values as tuple else -1
        return -1
      elif coord.x <= midpoint_value_x:
        for i in range(len(x_points)):
          if x_points[len(x_points)-i] == coord.x and y_points[len(x_points)-i] == coord.y:
            return (x_points[len(x_points)-i],y_points[len(x_points)-i])


        return -1
    try:
      
      x_to_be_removed, y_to_be_removed = linear_search(coord)
      
    except TypeError:
      raise IndexError("coord not inside line")
    
    self.x_points.remove(x_to_be_removed)
    self.y_points.remove(y_to_be_removed)


    return







#---------------------------------------
#begin functions




    
    

#plots coordinates in a txt file
def create_line_from_file(*,path: str, n_power: int=1, anomaly_check):
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
    
    line = Line(points, n_power)
    return line




    
#uses a list of tuples as coordinates
def create_line_from_raw(*,coords:list, n_power: int, anomaly_check):
  points = []
  if not callable(anomaly_check):
    raise TypeError("anomaly_check must be a function that has arguments: (x,y) which returns True if the point is an anomaly. ")
  for coord in coords:
    if not isinstance(coord, tuple):
      raise TypeError("all coodinates in provided list must be tuple")
    if len(coord) !=2:
      raise IndexError("all coordinates must only have length of 2 in form (x,y)")
    x,y = coord

    coord = Coordinate(x,y, anomaly_check(int(x),int(y)))
    points.append(coord)
  line = Line(points, n_power)

  return line



