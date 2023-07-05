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

duplicates_example = sequence[ sequence['id'] == '75977769' ]
# creates a list or series of rows that share the id number 75977769

print(" PATENT SEQUENCE FILE:\n ",duplicates_example)