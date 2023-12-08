# nearest-neighbors
This code creates an MxN dimensional boolean array with the number of positive values (ones) being determined by a specified density parameter. It then calculates nearest neighbors based on a distance parameter using the manhattan distance formula. Finally, it computes the total amount of neighboring cells in the array along with any overlapping cells.

> #### Solution Process
>
> 1. Allow the user to create an array of any size and fill with ones and zeros.
> 2. Determine the number of positive values (ones) on initiailization based on user input.
> 3. Get a list of positive value indexes. 
> 4. Loop through each positive value and find all neighboring pixels that meet the required distance threshold. Change corresponding pixel value based on its distance from the positive value index.
> 5. Get a count of neighboring pixels and overlapping pixels based on the pixels value.
> 6. Plot results cause plots are cool.
