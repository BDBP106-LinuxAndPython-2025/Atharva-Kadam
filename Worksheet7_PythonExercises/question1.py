"""(1) Create a module, CSVProcessor. It should contain functions for loading CSV data
from an external file (titanic.csv), calculating total number of columns, calculating total
number of rows and filling missing values in any column with zero. Use Pandas read csv
and other Pandas and Numpy functions. Import this module into another program and
demonstrate invoking these methods."""
import pandas as pd

import CSVProcessor as cp

df=cp.loading_csv_file('titanic.csv')

if df is not None:
    print(cp.columns(df))
    print(cp.rows(df))
    df_zero_values=cp.missing_values(df)
    print("The missing values filled with zero are:\n",df_zero_values["age"])
