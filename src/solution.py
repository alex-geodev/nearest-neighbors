import argparse
import random
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt            

def create_array(rows: int,cols: int, pos_value_density: float) -> np.array:
    '''Returns an array of zeros and ones.
    
    Inputs:

    rows (int): Number of rows in the array.
    cols (int): Number of cols in the array.
    pos_value_density (float): A number between 0-1 approximating 
    the percentage of ones in the array.
    
    Returns:
    array
    '''
    
    arr = np.random.rand(rows,cols)
    return (arr>1-pos_value_density).astype(float)

def is_within_distance(index: tuple,pos_val: list,distance: int) -> float:
    '''Calculates the distance of a single cell from the specified target cell.
 
    Inputs:
    
    index (tuple): A cell from the initialized array.
    pos_val (list): The positive cell used a centroid for the distance calculation.
    distance (int): The max distance to qualify as a neighbor.

    Returns:
    float:  A float is primarly used for plotting puposes.
    '''
    
    dist = abs(index[0]-pos_val[0]) +abs(index[1]-pos_val[1])

    #return a float to provide a gradient visualization of cell distance
    return 1/dist if 0<dist<=distance else 0

def detect_neighbors(init_array: np.array,pos_vals: list,distance: int):
    '''Iterates through the initialized array to find all neighbors 
    that meet the distance threshold.
 
    Inputs:
    
    init_array (array): The initialized array.
    pos_val (list): The positive cell used a centroid for the distance calculation.
    distance (int): The max distance to qualify as a neighbor.

    Returns:
    array:  The modified init_array with values > 0 correlating to neighbors.
      values = 2 are overlaps.
    '''
    mod_arr = init_array.copy()
    for value in pos_vals:
        arr_iterable = np.nditer(mod_arr, flags = ["multi_index"])

        for item in arr_iterable:
            if not item:
                mod_arr[arr_iterable.multi_index]=is_within_distance(arr_iterable.multi_index,value,distance)

            elif item !=1 and is_within_distance(arr_iterable.multi_index,value,distance):
                mod_arr[arr_iterable.multi_index]=2
    return mod_arr

def get_grid_counts(neighbors):
    '''Get count of true neighbors and overlaps.'''
    count= np.count_nonzero(neighbors)
    overlaps  = np.count_nonzero(neighbors[neighbors==2])
    return count,overlaps

def range_limited_float_type(arg):
    """ Type function for argparse - a float within bounds """
    try:
        f = float(arg)
    except ValueError:    
        raise argparse.ArgumentTypeError("Must be a floating point number")
    if f < 0 or f > 1:
        raise argparse.ArgumentTypeError("Argument must be between 0 and 1.")
    return f

def main():

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        'rows',type=int,nargs='?',default=50,
        help="The number of rows in the grid."
    )
    parser.add_argument(
        'cols', type=int,nargs='?', default=50,
        help = "The number of columns in the grid."
    )
    parser.add_argument(
        'distance', type=int, nargs='?', default=3,
        help= "The manhattan distance used to search for neighbors."
    )
    parser.add_argument(
        'pos_value_density',
        type=range_limited_float_type, nargs='?', default=0.01,
        help='Positive Value Density. A percentage to determine a density of positive \
            values within the grid.'
    )
    parser.add_argument(
        'plot_data',type=bool, nargs='?', default=1,
        help = 'Plot grid results'
    )

    args = parser.parse_args()

    init_arr = create_array(args.rows,args.cols,args.pos_value_density)
    print(init_arr.shape)
    pos_vals = np.dstack(np.where(init_arr>0))[0]

    neighbors=detect_neighbors(init_arr,pos_vals,args.distance)

    count, overlaps = get_grid_counts(neighbors)


    print(f'Total Neighbor Detections: {count}')
    print(f'Total Overlap Detections: {overlaps}')

    if args.plot_data:
        ax = sns.heatmap(neighbors, cbar=False)
        plt.show()


if __name__ == "__main__":
    main()