import random
import numpy as np

class Grid():
    def __init__(self, rows: int = random.randrange(1,100),
                  cols: int = random.randrange(1,100),
                  density: float = 0.98) -> np.array:
        
        self.rows = rows
        self.cols = cols
        self.density = density
        self.grid = np.random.rand(self.rows,self.cols)
        self.grid = (self.grid>self.density).astype(float)
    
def get_positive_values(self):
    self.pos_vals = np.dstack(np.where(self.grid>0))[0]

def determine_cell_distance(self,grid_index,pos_val,distance):
    cell_distance = abs(grid_index[0]-pos_val[0]) +abs(grid_index[1]-pos_val[1])
    return 1/cell_distance if 0<cell_distance<=distance else 0

def detect_neighbors(self,pos_vals,distance):

    mod_arr = self.grid.copy()
    for value in pos_vals:
        arr_iterable = np.nditer(mod_arr, flags = ["multi_index"])

        for item in arr_iterable:
            if not item:
                mod_arr[arr_iterable.multi_index]=determine_cell_distance(arr_iterable.multi_index,value,distance)

            elif item !=1 and determine_cell_distance(arr_iterable.multi_index,value,distance):
                mod_arr[arr_iterable.multi_index]=2
    return mod_arr
