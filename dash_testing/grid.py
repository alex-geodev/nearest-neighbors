import random
import numpy as np
from dataclasses import dataclass

@dataclass
class Grid():

    rows: int = random.randint(20,100)
    cols: int = random.randint(20,100)
    density: float = 0.02
    distance: int = 2

    def __post_init__(self):
        self.grid: np.array = self._create_grid()
        self.pos_vals: list = self._get_positive_values()

    def _create_grid(self):
        grid = np.random.rand(self.rows,self.cols)
        return (grid>1-self.density).astype(float)
    

    def _is_within_distance(self, index: tuple, value: int) -> float:
        #manhattan distance formula
        distance = abs(index[0]-value[0]) +abs(index[1]-value[1])
        return 1/distance if 0<distance<=self.distance else 0
    
    def _get_positive_values(self):
        return np.dstack(np.where(self.grid>0))[0]

    def detect_neighbors(self):
        #create modified array for testing/debugging comparisons against init_arr
        mod_arr = self.grid.copy()
        for value in self.pos_vals:
            arr_iterable = np.nditer(mod_arr, flags = ["multi_index"])

            for item in arr_iterable:
                if not item:
                    mod_arr[arr_iterable.multi_index] = self._is_within_distance(arr_iterable.multi_index,value)

                elif item !=1 and self._is_within_distance(arr_iterable.multi_index,value):
                    #set overlapping cells to a unique value for plotting purposes
                    mod_arr[arr_iterable.multi_index]=2
        self.neighbors = mod_arr
