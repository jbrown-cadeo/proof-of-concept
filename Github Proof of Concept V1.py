# Github Proof of Concept

# Packages
import pandas as pd
import numpy as np

# Load files

File1 = pd.read_csv(r'S:\Shared Folders\CADEO\06_Get Better\Analysis & Data Science\Project Ideas\Github\Example Building Summary.csv')
File2 = pd.read_csv(r'S:\Shared Folders\CADEO\06_Get Better\Analysis & Data Science\Project Ideas\Github\Example HVAC Summary.csv')

# Edit 1 - Replace NULL values with '0'

File1 = File1.fillna(0)
File2 = File2.fillna(0)

# Edit 2 - Replace '0' with "nan" for columns containing non-numerical values
print(File1.dtypes.value_counts()) # Identifies column types
print(File2.dtypes.value_counts()) # Identifies column types

col_objects1 = File1.dtypes[(File1.dtypes == 'object')].index.tolist()
for col in col_objects1:
    File1[col] = File1[col].replace(0,np.nan)
    
col_objects2 = File2.dtypes[(File2.dtypes == 'object')].index.tolist()
for col in col_objects2:
    File2[col] = File2[col].replace(0,np.nan)
    
# Save Version 1
    
File1.to_csv(r'S:\Shared Folders\CADEO\06_Get Better\Analysis & Data Science\Project Ideas\Github\Updated Building Summary V1.csv')
File2.to_csv(r'S:\Shared Folders\CADEO\06_Get Better\Analysis & Data Science\Project Ideas\Github\Updated HVAC Summary V1.csv')

# Ethan Wilkes
