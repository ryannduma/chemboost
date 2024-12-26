import pandas as pd
from matminer.datasets import load_dataset
from typing import Dict
import csv


def load_element_data(filename: str) -> Dict[str, float]:
    """Load element data from a CSV file.
    
    Args:
        filename (str): Path to the CSV file containing element data.
        
    Returns:
        Dict[str, float]: Dictionary mapping element symbols to their electronegativity values.
        
    Example:
        >>> element_data = load_element_data("element_data.csv")
        >>> print(element_data["Fe"])
        1.83
    """
    element_data = {}
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            element = row["element"]
            electronegativity = float(row["Electronegativity"]) 
            element_data[element] = electronegativity
    return element_data


def load_matbench_data():
    """Load and prepare the matbench experimental bandgap dataset.
    
    Loads the matbench_expt_gap dataset and adds a binary classification column
    'is_metal' based on the experimental bandgap values.
    
    Returns:
        pandas.DataFrame: DataFrame containing the matbench data with added 'is_metal' column.
        The 'is_metal' column is 1 for metals (zero bandgap) and 0 for non-metals.
    """
    df = load_dataset("matbench_expt_gap")
    df['is_metal'] = (df['gap expt'] == 0.0).astype(int)
    return df