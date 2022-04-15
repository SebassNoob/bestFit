import sys
sys.path.insert(1,'src/bestFit')
import main as bf



#init a line y=3x with 6 sets of "fitting coordinates"
#but with 2 extra that needs to be balanced
my_line = [(0,0),
          (1,3),
          (2,6),
          (3,9),
          (4,12),
          (5,15),
          (6,19),
          (6,17)]

line = bf.create_line_from_raw(coords = my_line, n_power= 1)

m,c = line.polynomial_coefficients
# m,c where y=mx+c
# m is gradient which should be 3 since y= 3x in all coordinates of my_line
assert (float(m)==3.0),"test failed"
print("test success")
