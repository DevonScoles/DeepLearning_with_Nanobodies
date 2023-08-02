import pandas as pd

# open files for reading/writing
merge = pd.read_csv('manual_merged.csv')

# Replace '018be3fea84601a90ea29295ef8bc4f0' with the ID to modify
target_id = '018be3fea84601a90ea29295ef8bc4f0'

# Modify the 'Human' column for the specific ID
merge.loc[merge['id'] == target_id, 'Human'] = True

merge.to_csv('manual_merged.csv', index=False)
