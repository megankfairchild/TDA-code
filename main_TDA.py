#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 15:17:59 2024

@author: meganfairchild

this is the main file to compute TDA for our data set
"""

#necessary preamble
import io
import pandas as pd
import numpy as np
import gudhi

#accompanying python scripts
import construct_complex as cc
import construct_mapper as cmapper 

#Step 1: import the CSV of the data set
dataset = "data_numerical_women.csv"  # whichever we are currently analyzing. make sure it is in the same folder as the script. 

"""
Step 2: we will ensure the dataset is what we are expecting. 
"""
data = pd.read_csv(dataset)
def load_and_validate_csv(filepath):
    try:
        df = pd.read_csv(filepath)
        if not np.issubdtype(df.to_numpy().dtype, np.number):
            raise ValueError("The CSV file contains non-numerical values.")
        data_array = df.to_numpy()
        if data_array.size == 0:
            raise ValueError("The CSV file is empty.")
        return data_array
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        raise
    except pd.errors.EmptyDataError:
        print("Error: The CSV file is empty.")
        raise
    except ValueError as e:
        print(f"Error: {e}")
        raise

if __name__ == "__main__": #if __name__ == "__main__": checks if the script is being run directly. If true, the code block following it will execute.
    filepath=dataset
    try:
        data_array = load_and_validate_csv(filepath)
        print("Data loaded successfully.")
        print(f"Data shape: {data_array.shape}")
        # Call other scripts or functions here
    except Exception as e:
        print(f"Failed to load and validate data: {e}")
    

# Step 3: Convert to a numpy array and normalize the data
data_array = data.to_numpy() 

def z_score_normalize(data): #the function to normalize the data
    mean_val = np.mean(data, axis=0)
    std_val = np.std(data, axis=0)
    normalized_data = (data - mean_val) / std_val
    return normalized_data

normalized_data = z_score_normalize(data_array)


#next hand the numpy array to GUDHI 

# Step 4: Compute a Rips complex
"""
change and edit the parameters for computing persistent homology here 
"""

max_dimension = 4 
max_edge_length = 6.0
output_file_barcodes = 'persistenceBarcodesMen.png'
output_file_graph = 'persistenceGraphMen.png'
# Call the function with the specified parameters
persistence = cc.construct_calculate(normalized_data, max_dimension, max_edge_length)

    


# Now compute the persistence barcodes or graph 
try:
    cc.persistence_barcodes(persistence, output_file_barcodes)
except Exception as e:
    print(f"An error occurred during the persistence barcodes: {e}")    


try:
    cc.persistence_graph(persistence, output_file_graph)
except Exception as e:
    print(f"An error occurred during the persistence graph: {e}")      



# Now mapper time
output_file_mapper = 'mapper_output_men.png'
num_intervals = 20
overlap_frac = 0.3
try:
    cmapper.construct_mapper_graph(normalized_data, num_intervals, overlap_frac, output_file_mapper)
except Exception as e:
    print(f"An error occurred during the persistence graph: {e}")  



"""
end of script
"""