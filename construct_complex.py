#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 10:20:50 2024

@author: meganfairchild

This script is for the construction of the simplicial complex
"""

import gudhi
import matplotlib.pyplot as plt
plt.rcParams['text.usetex'] = False #so we do not get the LaTeX error

def construct_calculate(data_array, max_dimension, max_edge_length):
    """
    Constructs a Vietoris-Rips complex, computes persistence, and visualizes the persistence diagram.
    
    Parameters:
    - data_array: numpy array of data points.
    - max_dimension: Maximum dimension of the simplices.
    - max_edge_length: Maximum edge length for the Rips complex.
    """
    try:
        # Check if the input data array is empty; if so, raise an error
        if data_array.size == 0:
            raise ValueError("Input data array is empty.")
        
        # Construct a Vietoris-Rips complex from the data points with the specified maximum edge length
        rips_complex = gudhi.RipsComplex(points=data_array, max_edge_length=max_edge_length)
        
        # Create a simplex tree from the Rips complex with the specified maximum dimension
        simplex_tree = rips_complex.create_simplex_tree(max_dimension=max_dimension)

        # Compute the persistence of the simplex tree (the birth and death of homological features)
        persistence = simplex_tree.persistence()
        
        # Print the persistence intervals to the console for debugging and verification
        #print(f"Persistence intervals: {persistence}")

        # Return the persistence intervals for further use if needed
        return persistence

    except Exception as e:
        # Catch any exception that occurs, print an error message, and re-raise the exception
        print(f"An error occurred: {e}")
        raise


"""
a function to compute the persistence barcodes
"""        
        
def persistence_barcodes(persistence, output_file):    
        # Visualize persistence barcode
        f, ax = plt.subplots(figsize=(10, 10))
        #plot the persistence barcodes
        gudhi.plot_persistence_barcode(persistence, axes=ax, legend=True)
        plt.savefig(output_file)
        print(f"Persistence barcode saved as {output_file}")     



"""
a function to compute the persistence graph
"""  




def persistence_graph(persistence, output_file):
        # Create a new figure and axis for plotting the persistence diagram with a specified size
        f, ax = plt.subplots(figsize=(10, 10))
        
        # Plot the persistence diagram using Gudhi's built-in function, with a legend
        gudhi.plot_persistence_diagram(persistence, axes=ax, legend=True)
        
        # Save the plot as an image file with the specified output file name
        plt.savefig(output_file)
        
        # Print a confirmation message that the persistence diagram was saved
        print(f"Persistence diagram saved as {output_file}")        








"""
end of script
"""