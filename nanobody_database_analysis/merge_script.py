import pandas as pd 

metaData = pd.read_csv('patent_meta.tsv', delimiter='\t')
sequence = pd.read_csv('patent_sequence.tsv', delimiter='\t')


sequence = sequence.rename(columns={'Comma-separated db-specific IDS': 'id'})
# renaming column name to id for easier access 
sequence = sequence[ ['id'] + [col for col in sequence.columns if col != 'id'] ]
# making 'id' the first column since 'id' is the first column in the metadata file
sequence['file type'] = 'patent sequence'
metaData['file type'] = 'patent metaData'
# giving the CSV files a new column for easier organization after merging


# ***
# When id column is a list of ids i.e. [3542135, 2351351]
# loop seperates them into individual rows with same sequence and CDR regions
# ***
for i,row in sequence.iterrows():
    id_num = row['id'] #id_num is the id for that row e.g. id_num = '72457245'
    if len(id_num.split(',')) > 1: # if multiple ids in the id column split them into a list
        id_list = id_num.split(',')
        for j, id in enumerate(id_list): #iterate through the list and give each id it's own row
            new_row = [ int(id),row['sequence'],row['CDR1'],row['CDR2'],row['CDR3'],row['file type'] ]
            sequence = sequence.iloc[:i+j, :].append(pd.Series(new_row, index=sequence.columns), ignore_index=True)

"""
import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('your_file.csv')

# Convert the "id" column to numeric values
df['id'] = pd.to_numeric(df['id'], errors='coerce')

# Sort the DataFrame based on the "id" column
df_sorted = df.sort_values(by='id')

# Write the sorted DataFrame back to a CSV file
df_sorted.to_csv('sorted_file.csv', index=False)
"""


sequence = sequence.sort_values(by='id')
metaData = metaData.sort_values('id')


# ***
# When multiple instances or rows of id exist
# loop appends -instance# onto the end e.g. 8731642-1 then 8731642-2 then 8731642-3...
# ***
sequence_dups = sequence['id'].duplicated()
suffixes = {}
for i,row in sequence.iterrows():
    id_value = row['id'] # id value = random num in 'id' column
    if sequence_dups[i]: # i = line from sequence file so here we check if that line is in the duplicated series
        if id_value in suffixes:
            suffixes[id_value] += 1
            sequence.at[i,'id'] = f"{id_value}-{suffixes[id_value]}"
        
        else:
            suffixes[id_value] = 1
            sequence.at[i,'id'] = f"{id_value}-{suffixes[id_value]}"

sequence.to_csv('patent_sequence_mod.csv', index=False)


# merge_test = pd.merge(metaData, sequence, on='id', how='outer')


# merged_file.to_csv('merge_test.csv', index=False)
