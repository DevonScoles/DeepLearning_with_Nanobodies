import pandas as pd

metaData = pd.read_csv('abgenbank_meta.tsv', delimiter='\t')
sequence = pd.read_csv('abgenbank_sequence.tsv', delimiter='\t')

sequence = sequence.rename(columns={'Comma-separated db-specific IDS': 'id'}) #rename column to just id
sequence = sequence[ ['id'] + [col for col in sequence.columns if col != 'id'] ] # sort left to right starting from id column

# ***
# When id column is a list of ids i.e. [3542135, 2351351]
# loop seperates them into individual rows with same sequence and CDR regions
# ***
for i,row in sequence.iterrows():
    id_num = row['id'] #id_num is the id for that row e.g. id_num = '72457245'
    if len(id_num.split(',')) > 1: # if multiple ids in the id column split them into a list
        id_list = id_num.split(',')
        for j, id in enumerate(id_list): #iterate through the list and give each id it's own row
            new_row = [ id,row['sequence'],row['CDR1'],row['CDR2'],row['CDR3'] ]
            sequence = sequence.iloc[:i+j, :].append(pd.Series(new_row, index=sequence.columns), ignore_index=True)

# Convert the "id" column to numeric values
sequence = sequence.sort_values('id')
metaData = metaData.sort_values('id')

sequence.to_csv('modified_abgenbank_sequence.tsv', sep='\t',index=False)
metaData.to_csv('modified_abgenbank_metadata.tsv', sep='\t',index=False)

