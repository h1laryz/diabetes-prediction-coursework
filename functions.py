import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import learning_curve

def zero_to_average(dataset, column):
    res = False
    for i, row in dataset.iterrows():
        if row[column] == 0:
            dataset.at[i, column] = round(dataset[column].mean(), 2)
            res = True
        
    
    if res:
        print("Found 0 in column:", column)
        
    return dataset


def check_values_under_zero(dataset, column):
    for i, row in dataset.iterrows():
        if row[column] < 0:
            print("Found value below 0 in column ", column)
            return True
    return False
