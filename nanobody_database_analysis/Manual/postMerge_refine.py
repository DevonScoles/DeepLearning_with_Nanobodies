import pandas as pd

# open files for reading/writing
merge = pd.read_csv('manual_merged.csv')

# Replace '018be3fea84601a90ea29295ef8bc4f0' with the ID to modify
target_id = '05783fe24e3caf0cfde8dd4c3abf165f'

# Modify the 'Human' column for the specific ID
merge.loc[merge['id'] == target_id, 'Human'] = False

merge.to_csv('manual_merged.csv', index=False)
