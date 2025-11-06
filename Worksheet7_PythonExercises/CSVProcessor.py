import numpy as np
import pandas as pd

def loading_csv_file(external_file):
    try:
        f_csv=pd.read_csv(external_file)
        return f_csv
    except FileNotFoundError:
        print("Input a valid file.")
        return None


def columns(f_csv):
    return f"The number of columns in the file are: {f_csv.shape[1]}"

def rows(f_csv):
    return f"The number of rows in the file are: {f_csv.shape[0]}"

def missing_values(f_csv):
    return f_csv.fillna(0)






