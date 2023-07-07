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

sequence_dups = sequence['id'].duplicated()
print(sequence.head())
print(sequence[sequence_dups])

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


sequence.to_csv('modified_sequence.csv', index=False)

