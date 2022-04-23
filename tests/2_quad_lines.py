import sys
sys.path.insert(1,'src/bestFit')
import main as bf
import time


line = bf.create_line_from_raw(coords = [(0,1),(9,2),(1,3),(4,7),(2,12),(-12,-2),(0,-2)], n_power = 2, linestyle = "b--")


line2 = bf.create_line_from_raw(coords = [(0,4),(2,3),(1,15),(3,2),(9,22),(-12,-4),(0,-6)], n_power = 2, linestyle = "g-")
line2.plot()
line.add_point(bf.Coordinate(100,0))
line.remove_point(bf.Coordinate(-12,-2))
smooth = line.smoothen_line(10)
line.plot()


bf.show_graph()
time.sleep(10)

bf.save_fig("./graph")
